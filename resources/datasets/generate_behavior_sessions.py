"""Generate a synthetic multilevel behavioral dataset for the course.

Standard library only, so anyone can regenerate it with no installs:

    python3 generate_behavior_sessions.py

The data are made up. They are designed to have a nested (multilevel) structure
so a mixed-effects model is the natural choice: repeated sessions are nested
within participants, and participants are nested within clinics. The generating
model below is the "ground truth" the analysis should be able to recover, which
makes it useful for checking whether an analysis is doing the right thing.
"""

import csv
import random

SEED = 20260605
N_CLINICS = 4
PARTICIPANTS_PER_CLINIC = 8
N_SESSIONS = 12
BASELINE_SESSIONS = 6  # sessions 1..6 are baseline, 7..12 are intervention

# Fixed effects (the ground truth)
INTERCEPT = 8.0           # baseline target rate (responses per minute)
EFFECT_INTERVENTION = -3.0  # intervention lowers the rate
EFFECT_SESSION = -0.10    # slight decline across sessions on its own
EFFECT_SEVERITY = 0.25    # higher baseline severity, higher rate
EFFECT_AGE = -0.02        # very small age effect (weak on purpose)

# Random-effect standard deviations
SD_CLINIC = 1.5           # clinic-level intercept
SD_PARTICIPANT = 2.0      # participant-level intercept
SD_PARTICIPANT_SLOPE = 0.15  # participant-level slope on session
SD_RESIDUAL = 1.0         # observation-level noise


def main():
    rng = random.Random(SEED)
    rows = []

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

            for s in range(1, N_SESSIONS + 1):
                condition = "baseline" if s <= BASELINE_SESSIONS else "intervention"
                intervention_on = 0 if condition == "baseline" else 1

                mean = (
                    INTERCEPT
                    + clinic_intercept
                    + participant_intercept
                    + EFFECT_INTERVENTION * intervention_on
                    + (EFFECT_SESSION + participant_slope) * s
                    + EFFECT_SEVERITY * (baseline_severity - 5)
                    + EFFECT_AGE * (age - 25)
                )
                rate = mean + rng.gauss(0, SD_RESIDUAL)
                rate = max(0.0, rate)  # a rate cannot be negative

                rows.append(
                    {
                        "clinic_id": clinic_id,
                        "participant_id": participant_id,
                        "age": age,
                        "baseline_severity": baseline_severity,
                        "session": s,
                        "condition": condition,
                        "target_rate": round(rate, 2),
                    }
                )

    fieldnames = [
        "clinic_id",
        "participant_id",
        "age",
        "baseline_severity",
        "session",
        "condition",
        "target_rate",
    ]
    with open("behavior_sessions.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote behavior_sessions.csv with {len(rows)} rows.")


if __name__ == "__main__":
    main()
