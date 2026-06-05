"""Generate a synthetic multilevel behavioral dataset for the course.

Standard library only, so anyone can regenerate it with no installs:

    python3 generate_behavior_sessions.py

The data are made up. They are designed to have a nested (multilevel) structure
with four levels, so a mixed-effects model is the natural choice:

    minute  ->  session  ->  participant  ->  clinic

That is, responses are counted in one-minute intervals within a session, sessions
repeat within a participant, and participants sit within a clinic. Within a session
the per-minute counts also form a short time series with autocorrelation, so
successive minutes are not independent. This is realistic and sets up the
independence-assumption discussion in Week 8.

The script writes two files at two grains, both from the same generating model:

    behavior_intervals.csv   one row per minute (the finest grain, with the
                             within-session time series)
    behavior_sessions.csv    one row per session (the per-minute counts aggregated
                             to a session rate); identical schema to before

Because the data come from a known model, an analysis can be checked against the
values that actually produced them.
"""

import csv
import math
import random

SEED = 20260605
N_CLINICS = 4
PARTICIPANTS_PER_CLINIC = 8
N_SESSIONS = 12
BASELINE_SESSIONS = 6   # sessions 1..6 are baseline, 7..12 are intervention
N_MINUTES = 10          # one-minute intervals within each session

# Fixed effects (the ground truth), on a responses-per-minute scale
INTERCEPT = 8.0            # baseline per-minute rate
EFFECT_INTERVENTION = -3.0  # intervention lowers the rate
EFFECT_SESSION = -0.10    # slight decline across sessions on its own
EFFECT_SEVERITY = 0.25    # higher baseline severity, higher rate
EFFECT_AGE = -0.02        # very small age effect (weak on purpose)

# Random-effect standard deviations
SD_CLINIC = 1.5           # clinic-level intercept
SD_PARTICIPANT = 2.0      # participant-level intercept
SD_PARTICIPANT_SLOPE = 0.15      # participant-level slope across sessions
SD_PARTICIPANT_WS_SLOPE = 0.10   # participant-level within-session slope

# Within-session structure
WS_SLOPE_INTERVENTION = -0.40  # within-session decline under intervention
WS_SLOPE_BASELINE = 0.00       # roughly flat within a baseline session
AR1_PHI = 0.40            # autocorrelation between successive minutes
SD_AR1 = 0.80             # innovation noise for the AR(1) series


def poisson(rng, lam):
    """Draw a Poisson count using Knuth's algorithm (no numpy needed)."""
    if lam <= 0:
        return 0
    target = math.exp(-lam)
    k = 0
    p = 1.0
    while True:
        k += 1
        p *= rng.random()
        if p <= target:
            return k - 1


def main():
    rng = random.Random(SEED)
    interval_rows = []
    session_rows = []

    for c in range(1, N_CLINICS + 1):
        clinic_id = f"C{c}"
        clinic_intercept = rng.gauss(0, SD_CLINIC)

        for p in range(1, PARTICIPANTS_PER_CLINIC + 1):
            pid_num = (c - 1) * PARTICIPANTS_PER_CLINIC + p
            participant_id = f"P{pid_num:02d}"

            age = rng.randint(6, 45)
            baseline_severity = rng.randint(1, 10)
            participant_intercept = rng.gauss(0, SD_PARTICIPANT)
            participant_slope = rng.gauss(0, SD_PARTICIPANT_SLOPE)
            participant_ws_slope = rng.gauss(0, SD_PARTICIPANT_WS_SLOPE)

            for s in range(1, N_SESSIONS + 1):
                condition = "baseline" if s <= BASELINE_SESSIONS else "intervention"
                intervention_on = 0 if condition == "baseline" else 1

                session_mean_rate = (
                    INTERCEPT
                    + clinic_intercept
                    + participant_intercept
                    + EFFECT_INTERVENTION * intervention_on
                    + (EFFECT_SESSION + participant_slope) * s
                    + EFFECT_SEVERITY * (baseline_severity - 5)
                    + EFFECT_AGE * (age - 25)
                )

                ws_base = (
                    WS_SLOPE_INTERVENTION if intervention_on else WS_SLOPE_BASELINE
                )
                ws_slope = ws_base + participant_ws_slope

                ar = 0.0
                total_responses = 0
                for m in range(1, N_MINUTES + 1):
                    ar = AR1_PHI * ar + rng.gauss(0, SD_AR1)
                    mu = session_mean_rate + ws_slope * (m - 1) + ar
                    mu = max(0.05, mu)  # expected count must be positive
                    responses = poisson(rng, mu)
                    total_responses += responses

                    interval_rows.append(
                        {
                            "clinic_id": clinic_id,
                            "participant_id": participant_id,
                            "age": age,
                            "baseline_severity": baseline_severity,
                            "session": s,
                            "condition": condition,
                            "minute": m,
                            "responses": responses,
                        }
                    )

                session_rows.append(
                    {
                        "clinic_id": clinic_id,
                        "participant_id": participant_id,
                        "age": age,
                        "baseline_severity": baseline_severity,
                        "session": s,
                        "condition": condition,
                        "target_rate": round(total_responses / N_MINUTES, 2),
                    }
                )

    interval_fields = [
        "clinic_id",
        "participant_id",
        "age",
        "baseline_severity",
        "session",
        "condition",
        "minute",
        "responses",
    ]
    with open("behavior_intervals.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=interval_fields)
        writer.writeheader()
        writer.writerows(interval_rows)

    session_fields = [
        "clinic_id",
        "participant_id",
        "age",
        "baseline_severity",
        "session",
        "condition",
        "target_rate",
    ]
    with open("behavior_sessions.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=session_fields)
        writer.writeheader()
        writer.writerows(session_rows)

    print(
        f"Wrote behavior_intervals.csv with {len(interval_rows)} rows and "
        f"behavior_sessions.csv with {len(session_rows)} rows."
    )


if __name__ == "__main__":
    main()
