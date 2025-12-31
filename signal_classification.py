import pandas as pd

# Load signal data (recompute from Phase 2 logic)
data = pd.read_csv("daily_data.csv")

baseline = {
    "sleep_avg": data["sleep_hours"].mean(),
    "sleep_std": data["sleep_hours"].std(),
    "steps_avg": data["steps"].mean(),
    "steps_std": data["steps"].std(),
    "screen_avg": data["screen_time_hours"].mean(),
    "screen_std": data["screen_time_hours"].std(),
    "workout_avg": data["workout_minutes"].mean(),
    "workout_std": data["workout_minutes"].std(),
    "study_avg": data["study_hours"].mean(),
    "study_std": data["study_hours"].std(),
}

def z_score(value, mean, std):
    if std == 0:
        return 0
    return (value - mean) / std

THRESHOLD = 2.0
classified_signals = []

for _, row in data.iterrows():
    day_events = []

    metrics = {
        "sleep": (row["sleep_hours"], baseline["sleep_avg"], baseline["sleep_std"]),
        "steps": (row["steps"], baseline["steps_avg"], baseline["steps_std"]),
        "screen time": (row["screen_time_hours"], baseline["screen_avg"], baseline["screen_std"]),
        "workout": (row["workout_minutes"], baseline["workout_avg"], baseline["workout_std"]),
        "study time": (row["study_hours"], baseline["study_avg"], baseline["study_std"]),
    }

    for metric, (value, mean, std) in metrics.items():
        z = z_score(value, mean, std)
        if z >= THRESHOLD:
            day_events.append(f"{metric} unusually high")
        elif z <= -THRESHOLD:
            day_events.append(f"{metric} unusually low")

    if day_events:
        classified_signals.append({
            "day": int(row["day"]),
            "signals": day_events
        })

print("Classified behavioral signals:")
for entry in classified_signals:
    print(f"Day {entry['day']}:")
    for s in entry["signals"]:
        print(f" - {s}")
