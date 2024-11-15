import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate date range
start_date = datetime.strptime("07-01-2024", "%m-%d-%Y")
end_date = datetime.strptime("11-01-2024", "%m-%d-%Y")
date_range = pd.date_range(start_date, end_date, freq='D')



# Adjust sleep data to be in minutes and re-generate wake status with 95% "No Wake Event" and 5% "Wake Event"
total_sleep_minutes = np.random.uniform(6 * 60, 8 * 60, len(date_range))  # Total sleep in minutes
rem_sleep_minutes = np.random.uniform(45, 120, len(date_range))  # REM sleep in minutes
deep_sleep_minutes = np.random.uniform(40, 120, len(date_range))  # Deep sleep in minutes
wake_status_adjusted = np.random.choice(["No Wake Event", "Wake Event"], len(date_range), p=[0.95, 0.05])

# Create updated DataFrame with adjusted values
sleep_data_minutes = pd.DataFrame({
    "Date": date_range,
    "Total Sleep": total_sleep_minutes,
    "REM Sleep": rem_sleep_minutes,
    "Deep Sleep": deep_sleep_minutes,
    "Wake Status": wake_status_adjusted
})

# Save the updated DataFrame to a new CSV
csv_path_minutes = './sleep_data_minutes.csv'
sleep_data_minutes.to_csv(csv_path_minutes, index=False)

