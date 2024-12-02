import xml.etree.ElementTree as ET
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import json
from matplotlib.dates import DateFormatter, MonthLocator

# Helper function to convert minutes to hours and minutes
def minutes_to_hours_and_minutes(minutes):
    hours = int(minutes // 60)
    remaining_minutes = int(minutes % 60)
    return f"{hours} hours and {remaining_minutes} minutes"

# SECTION 1: Load and Preprocess Data
def load_and_preprocess_data(xml_file):
    # Parse XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract and preprocess records
    record_list = [x.attrib for x in root.iter('Record')]
    data = pd.DataFrame(record_list)

    for col in ['creationDate', 'startDate', 'endDate']:
        data[col] = pd.to_datetime(data[col])

    data['value'] = pd.to_numeric(data['value'], errors='coerce').fillna(1.0)
    data['type'] = data['type'].str.replace('HKQuantityTypeIdentifier', '').str.replace('HKCategoryTypeIdentifier', '')

    return data

# SECTION 2: Filter and Aggregate Sleep Data
def process_sleep_data(data):
    # Filter for sleep analysis from a specific source
    sleep_data = data[data['type'] == "SleepAnalysis"]
    sleep_data = sleep_data[sleep_data['sourceName'] == "Eight Sleep"]

    # Calculate derived metrics
    sleep_data['time_asleep'] = sleep_data['endDate'] - sleep_data['startDate']
    sleep_data = sleep_data[sleep_data['creationDate'] < pd.Timestamp("2024-10-01", tz="UTC-08:00")]

    # Group and aggregate data
    sleep_data = sleep_data.groupby('creationDate').agg(
        total_time_asleep=('time_asleep', 'sum'),
        bed_time=('startDate', 'min'),
        awake_time=('endDate', 'max'),
        sleep_counts=('creationDate', 'count'),
        rem_cycles=pd.NamedAgg(column='time_asleep', aggfunc=lambda x: (x // datetime.timedelta(minutes=90)).sum())
    )

    # Calculate additional metrics
    sleep_data['time_in_bed'] = (sleep_data['awake_time'] - sleep_data['bed_time']).dt.total_seconds() / 60
    sleep_data['total_time_asleep'] = sleep_data['total_time_asleep'].dt.total_seconds() / 60
    sleep_data['restless_time'] = sleep_data['time_in_bed'] - sleep_data['total_time_asleep']

    # Filter out corrupted data and scale time in bed
    sleep_data = sleep_data[(sleep_data['time_in_bed'] <= 1250) & (sleep_data['total_time_asleep'] <= 1250)]
    sleep_data['total_time_asleep'] = sleep_data['total_time_asleep'] / 2

    return sleep_data

# SECTION 3: Analyze and Display Results
def analyze_and_display(sleep_data):
    # Generate plots
    sleep_data[['time_in_bed', 'total_time_asleep']].plot(title="Time in Bed vs Total Time Asleep")
    plt.ylabel("Minutes")
    plt.show()

    # Calculate averages
    average_total_time_asleep = sleep_data['total_time_asleep'].mean()
    average_rem_cycles = sleep_data['rem_cycles'].mean()
    average_time_in_bed = sleep_data['time_in_bed'].mean()

    # Convert averages to hours and minutes
    average_total_time_asleep_str = minutes_to_hours_and_minutes(average_total_time_asleep)
    average_time_in_bed_str = minutes_to_hours_and_minutes(average_time_in_bed)
    average_time_in_rem = minutes_to_hours_and_minutes(average_rem_cycles * 25)

    # Print results
    print(f"Average Total Time Asleep per Day: {average_total_time_asleep_str}")
    print(f"Average REM Cycles per Day: {average_rem_cycles:.2f}")
    print(f"Average Time in Bed per Day: {average_time_in_bed_str}")
    print(f"Average Time in REM: {average_time_in_rem}")

    # Calculate and print the percentage of REM sleep
    rem_sleep_percentage = (average_rem_cycles * 25 / average_total_time_asleep) * 100
    print(f"Percentage of REM Sleep: {rem_sleep_percentage:.2f}%")

# SECTION 4: Save User Profile
def save_user_profile():
    user_profile = {
        "user_id": "",
        "age": "",
        "gender": "",
        "weight_kg": "",
        "height_cm": "",
        "activity_level": "",
        "self_reported_issues": [],
        "sleep_goals": {
            "target_sleep_duration": "",
            "target_bedtime": "",
            "target_wake_time": ""
        },
        "current_status": {
            "current_phase": "",
            "day_in_cycle": "",
            "days_until_next_period": "",
            "current_symptoms": [],
            "current_metrics": {
                "energy_level": "",
                "mood": "",
                "sleep_quality": "",
                "exercise_tolerance": ""
            }
        }
    }

    with open('user_profile.json', 'w') as json_file:
        json.dump(user_profile, json_file, indent=4)
    print("User profile saved to user_profile.json")

# Main Execution
if __name__ == "__main__":
    # Load and process data
    data = load_and_preprocess_data('export.xml')
    sleep_data = process_sleep_data(data)

    # Analyze and display results
    analyze_and_display(sleep_data)

    # Save user profile
    save_user_profile()