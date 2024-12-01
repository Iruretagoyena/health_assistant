import xml.etree.ElementTree as ET
import pandas as pd
import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import json
from matplotlib.dates import DateFormatter, MonthLocator



tree = ET.parse('export.xml')
root = tree.getroot()
record_list = [x.attrib for x in root.iter('Record')]
data = pd.DataFrame(record_list)
# data.head(10)

for col in ['creationDate', 'startDate', 'endDate']:
    data[col] = pd.to_datetime(data[col])

data['value'] = pd.to_numeric(data['value'], errors='coerce')
data['value'] = data['value'].fillna(1.0)
data['type'] = data['type'].str.replace('HKQuantityTypeIdentifier', '')
data['type'] = data['type'].str.replace('HKCategoryTypeIdentifier', '')

data.to_feather("apple_export.ftr")

sleep_data = data[data['type'] == "SleepAnalysis"]
sleep_data = sleep_data[sleep_data['sourceName'] == "Eight Sleep"]

sleep_data['time_asleep'] = sleep_data['endDate'] - sleep_data['startDate']

sleep_data = sleep_data.groupby('creationDate').agg(total_time_asleep=('time_asleep', 'sum'),
    bed_time=('startDate', 'min'),
    awake_time=('endDate', 'max'),
    sleep_counts=('creationDate','count'),
    rem_cycles=pd.NamedAgg(column='time_asleep', aggfunc=lambda x: (x // datetime.timedelta(minutes=90)).sum()))

sleep_data['time_in_bed'] = sleep_data['awake_time'] - sleep_data['bed_time']
sleep_data['restless_time'] = sleep_data['time_in_bed'] - sleep_data['total_time_asleep']
sleep_data['time_in_bed'] = (sleep_data['time_in_bed'].dt.total_seconds()/60)
sleep_data['total_time_asleep'] = (sleep_data['total_time_asleep'].dt.total_seconds()/60)

chart1 = sleep_data[['time_in_bed','total_time_asleep']].plot(use_index=True)


# Basic user information
user_profile = {
    "user_id": "",
    "age": "",
    "gender": "",
    "weight_kg": "",
    "height_cm": "",
    "activity_level": "",  # sedentary, moderate, active
    "self_reported_issues": [],

    # Goals and preferences
    "sleep_goals": {
        "target_sleep_duration": "",
        "target_bedtime": "",
        "target_wake_time": ""
    },

    # Cycle data
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
    },

    # Consistent Patterns (Based on Last 3 Cycles)
    "consistent_patterns": {
        "cycle_length": "",
        "phase_specific_patterns": {
            "menstrual": {
                "duration": "",
                "energy": "",
                "sleep": "",
                "exercise_tolerance": "",
                "key_symptoms": []
            },
            "follicular": {
                "energy": "",
                "sleep": "",
                "exercise_tolerance": "",
                "key_symptoms": []
            },
            "ovulatory": {
                "energy": "",
                "sleep": "",
                "exercise_tolerance": "",
                "key_symptoms": []
            },
            "luteal": {
                "energy": "",
                "sleep": "",
                "exercise_tolerance": "",
                "key_symptoms": []
            }
        }
    }
}

def get_user_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        else:
            print("This field cannot be empty. Please enter a valid value.")

def get_user_profile(user_profile):
    user_profile["user_id"] = get_user_input("Enter user ID: ")
    user_profile["age"] = get_user_input("Enter age: ")
    user_profile["gender"] = get_user_input("Enter gender: ")
    user_profile["weight_kg"] = get_user_input("Enter weight (kg): ")
    user_profile["height_cm"] = get_user_input("Enter height (cm): ")
    user_profile["activity_level"] = get_user_input("Enter activity level (sedentary, moderate, active): ")


    while True:
        issue = input("Enter a self-reported issue (or press Enter to finish): ")
        if issue.strip():
            user_profile["self_reported_issues"].append(issue)
        else:
            break

    return user_profile

user_profile = get_user_profile(user_profile)
print("User profile created:", user_profile)


plt.show()

print(user_profile)
# Save the user profile to a JSON file
with open('user_profile.json', 'w') as json_file:
    json.dump(user_profile, json_file, indent=4)

print("User profile saved to user_profile.json")