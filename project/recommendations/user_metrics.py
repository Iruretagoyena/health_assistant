import pandas as pd
import numpy as np
import json
from biological_age_recommendations import *
from analyze_results import *
from analyze_blood_work import *

# Load the CSV file into a DataFrame
csv_path = '../preprocessing/data/blood_test_results.csv'
data = pd.read_csv(csv_path)

# Define a dictionary that maps test names to their corresponding analysis functions
analysis_functions = {
    "Hemoglobin": analyze_hemoglobin,
    "Hematocrit": analyze_hematocrit,
    "Mean Cell Hemoglobin": analyze_mean_cell_hemoglobin,
    "Mean Cell Hemoglobin Concentration": analyze_mean_cell_hemoglobin_concentration,
    "Mean Cell Volume": analyze_mean_cell_volume,
    "Red Blood Cells": analyze_red_blood_cells,
    "Basophils": analyze_basophils,
    "Eosinophils": analyze_eosinophils,
    "Lymphocytes": analyze_lymphocytes,
    "Monocytes": analyze_monocytes,
    "Neutrophils": analyze_neutrophils,
    "White Blood Cells": analyze_white_blood_cells,
    "Platelets": analyze_platelets,
    "Ferritin": analyze_ferritin,
    "Total Cholesterol": analyze_total_cholesterol,
    "LDL Cholesterol": analyze_ldl_cholesterol,
    "HDL Cholesterol": analyze_hdl_cholesterol,
    "Triglycerides": analyze_triglycerides,
    "Glucose": analyze_glucose,
    "HbA1c": analyze_hba1c,
    "Creatinine": analyze_creatinine,
    # Add more mappings for each indicator
}

# Initialize an empty list to collect all recommendations
recommendations = []

# Loop through each row in the DataFrame and apply the corresponding analysis function
for _, row in data.iterrows():
    test_name = row["Test"]
    value = row["Quantitative"]

    # Check if the test has an associated analysis function
    if test_name in analysis_functions:
        # Call the analysis function and append its result to recommendations
        analysis_function = analysis_functions[test_name]
        recommendation = analysis_function(value)
        recommendations.append(recommendation)

# Combine all recommendations into a single text
combined_recommendations = "\n".join(recommendations)

# Display the combined recommendations
combined_recommendations


# Print recommendations and save to a file
with open('../output/recommendations.txt', 'w') as rec_outfile:
    for rec in recommendations:
        print(rec)
        rec_outfile.write(rec + '\n')

print("DEBUG - Recommendations generated.")









"""
    for _, record in data.iterrows():
        user = record.get('user_id', 'unknown')
        sleep_hours = record.get('sleep_hours', 0)
        steps = record.get('steps', 0)
        glucose_level = record.get('glucose_level', 100)
        vitamin_b12 = record.get('vitamin_b12', 400)
        bmi = record.get('bmi', 22)
        age = record.get('age', 30)
        weekly_activity = record.get('weekly_activity_minutes', 0)
        aging_rate = record.get('aging_rate', 1.0)
        social_count = record.get('social_interactions', 0)
        perception_score = record.get('perception_score', 5)
        telomere_length = record.get('telomere_length', 7.5)
        hba1c = record.get('hba1c', 5.4)
        rmr = record.get('rmr', 1600)
        vo2max = record.get('vo2max', 40)

        # Call modular functions
        recommendations.append(f"[User: {user}] {analyze_sleep(sleep_hours)}")
        recommendations.append(f"[User: {user}] {analyze_steps(steps)}")
        recommendations.append(f"[User: {user}] {analyze_glucose(glucose_level)}")
        recommendations.append(f"[User: {user}] {analyze_vitamin_b12(vitamin_b12)}")
        recommendations.append(f"[User: {user}] {analyze_bmi(bmi, age)}")
        recommendations.append(f"[User: {user}] {analyze_weekly_activity(weekly_activity)}")
        recommendations.append(f"[User: {user}] {analyze_aging_rate(aging_rate)}")
        recommendations.append(f"[User: {user}] {analyze_social_interaction(social_count)}")
        recommendations.append(f"[User: {user}] {analyze_perception_score(perception_score)}")
        recommendations.append(f"[User: {user}] {analyze_telomere_length(telomere_length)}")
        recommendations.append(f"[User: {user}] {analyze_hba1c(hba1c)}")
        recommendations.append(f"[User: {user}] {analyze_rmr(rmr)}")
        recommendations.append(f"[User: {user}] {analyze_vo2max(vo2max)}")

"""