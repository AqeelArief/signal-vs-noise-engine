import pandas as pd

# Load daily data
data = pd.read_csv("daily_data.csv")

# Calculate baseline statistics
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
    "study_std": data["study_hours"].std()
}

print("Baseline behavior summary:")
for key, value in baseline.items():
    print(f"{key}: {value:.2f}")
