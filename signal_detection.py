import pandas as pd

# Load data
data = pd.read_csv("daily_data.csv")

# Compute baseline stats
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

# Z-score function
def z_score(value, mean, std):
    if std == 0:
        return 0
    return (value - mean) / std

signals = []

for _, row in data.iterrows():
    day_signals = {}

    day_signals["sleep_z"] = z_score(row["sleep_hours"], baseline["sleep_avg"], baseline["sleep_std"])
    day_signals["steps_z"] = z_score(row["steps"], baseline["steps_avg"], baseline["steps_std"])
    day_signals["screen_z"] = z_score(row["screen_time_hours"], baseline["screen_avg"], baseline["screen_std"])
    day_signals["workout_z"] = z_score(row["workout_minutes"], baseline["workout_avg"], baseline["workout_std"])
    day_signals["study_z"] = z_score(row["study_hours"], baseline["study_avg"], baseline["study_std"])

    signals.append({
        "day": int(row["day"]),
        **day_signals
    })

signal_df = pd.DataFrame(signals)
print("Z-score signal analysis:")
print(signal_df)
