import pandas as pd

data = pd.read_csv("daily_data.csv")

baseline = {
    "sleep": (data["sleep_hours"].mean(), data["sleep_hours"].std()),
    "steps": (data["steps"].mean(), data["steps"].std()),
    "screen": (data["screen_time_hours"].mean(), data["screen_time_hours"].std()),
    "workout": (data["workout_minutes"].mean(), data["workout_minutes"].std()),
    "study": (data["study_hours"].mean(), data["study_hours"].std()),
}

def z_score(value, mean, std):
    if std == 0:
        return 0
    return (value - mean) / std

THRESHOLD = 2.0
MAX_ALERTS_PER_DAY = 2

alerts = []

for _, row in data.iterrows():
    day_alerts = []

    metrics = {
        "Sleep change": ("sleep", row["sleep_hours"]),
        "Step count change": ("steps", row["steps"]),
        "Screen time change": ("screen", row["screen_time_hours"]),
        "Workout activity change": ("workout", row["workout_minutes"]),
        "Study time change": ("study", row["study_hours"]),
    }

    for label, (key, value) in metrics.items():
        mean, std = baseline[key]
        z = z_score(value, mean, std)

        if abs(z) >= THRESHOLD:
            severity = abs(z)
            day_alerts.append({
                "alert": label,
                "severity": round(severity, 2),
                "direction": "high" if z > 0 else "low"
            })

    # Sort alerts by severity (most important first)
    day_alerts.sort(key=lambda x: x["severity"], reverse=True)

    # Keep only top alerts
    for alert in day_alerts[:MAX_ALERTS_PER_DAY]:
        alerts.append({
            "day": int(row["day"]),
            **alert
        })

print("Prioritized Alerts:")
for a in alerts:
    print(
        f"Day {a['day']}: {a['alert']} "
        f"({a['direction']}, severity={a['severity']})"
    )
