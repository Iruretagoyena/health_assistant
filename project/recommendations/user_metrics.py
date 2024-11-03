import pandas as pd
import numpy as np
import json
from biological_age_recommendations import *
# Individual analysis functions with enhanced logic

def analyze_sleep(sleep_hours, rem_sleep=None, deep_sleep=None):
    print(f"Debug - Sleep analysis: sleep_hours={sleep_hours}, rem_sleep={rem_sleep}, deep_sleep={deep_sleep}")
    # Check for insufficient sleep and provide recommendations
    if sleep_hours < 5:
        return "We need to pay attention to our sleep. Sleep is the #1 most important habit for your health and well-being. Consider a consistent sleep schedule and reducing blue light exposure before bed."
    # Check for slightly insufficient sleep and suggest improvements
    elif 5 <= sleep_hours < 6:
        return "You are getting some sleep, but it’s still not enough. Aim for at least 7 hours and consider relaxing evening routines like reading or meditation."
    # Check for moderate sleep with potential improvements for REM sleep
    elif 6 <= sleep_hours < 7:
        if rem_sleep and rem_sleep < 1.5:
            return "Good job on getting over 6 hours of sleep, but try to increase your REM sleep for better cognitive recovery."
        return "Good job on getting over 6 hours of sleep, but try pushing for 7-8 hours for optimal recovery."
    # Check for ideal sleep range and suggest deep sleep improvements
    elif 7 <= sleep_hours <= 8:
        if deep_sleep and deep_sleep < 1:
            return "Great job on your sleep schedule! You’re within the ideal range. Aim to increase deep sleep for muscle repair."
        return "Great job on your sleep schedule! You’re within the ideal range."
    # Handle cases where sleep exceeds 8 hours
    else:
        return "Sleeping more than 8 hours might indicate fatigue or other issues. Monitor your energy levels and sleep quality."

def analyze_steps(steps, pace=None, heart_rate=None):
    print(f"Debug - Steps analysis: steps={steps}, pace={pace}, heart_rate={heart_rate}")
    # Check for high step count and provide personalized advice
    if steps >= 10000:
        if pace and pace < 3:
            return "Congratulations for nailing 10k steps a day this week! Consider increasing your pace for better cardiovascular benefits."
        return "Congratulations for nailing 10k steps a day this week! Keep maintaining this level of activity."
    # Check for low step count and provide motivation with safety checks
    elif steps < 5000:
        if heart_rate and heart_rate > 100:
            return "Try to increase your daily activity, but monitor your heart rate to ensure safe exertion. Walking at least 5,000 steps a day can boost your overall health."
        return "Try to increase your daily activity. Walking at least 5,000 steps a day can boost your overall health."
    # Advise on maintaining moderate step count
    else:
        return "Keep pushing for more steps to enhance your fitness. Aim for at least 30 minutes of brisk walking."

def analyze_glucose(glucose_level, fasting_glucose=None):
    print(f"Debug - Glucose analysis: glucose_level={glucose_level}, fasting_glucose={fasting_glucose}")
    # Check for high glucose and suggest interventions
    if glucose_level > 140:
        return "Your glucose levels are high. Implement a low-glycemic diet and consider speaking with a healthcare provider."
    # Check for low glucose and provide safety advice
    elif glucose_level < 70:
        return "Your glucose levels are low. Monitor your diet and consult a specialist if needed. Ensure you’re not skipping meals."
    # Provide recommendations for managing borderline fasting glucose
    else:
        if fasting_glucose and fasting_glucose > 100:
            return "Your glucose levels are within a healthy range, but consider improving fasting glucose with dietary fiber and exercise."
        return "Your glucose levels are within a healthy range."

def analyze_vitamin_b12(vitamin_b12):
    print(f"Debug - Vitamin B12 analysis: vitamin_b12={vitamin_b12}")
    # Check for vitamin B12 deficiency and provide dietary advice
    if vitamin_b12 < 200:
        return "Your vitamin B12 levels seem low. Consider foods rich in B12 like fish, meat, and fortified cereals or supplementation."
    # Warn about borderline B12 levels
    elif 200 <= vitamin_b12 < 400:
        return "Your vitamin B12 levels are on the lower side. Maintain a balanced diet with B12-rich foods."
    else:
        return "Your vitamin B12 levels are adequate. Maintain your current diet."

def analyze_bmi(bmi, age, body_fat=None):
    print(f"Debug - BMI analysis: bmi={bmi}, age={age}, body_fat={body_fat}")
    # Check for high BMI and correlate with body fat percentage for more targeted advice
    if bmi > 25 and age > 30:
        if body_fat and body_fat > 25:
            return "Your BMI and body fat percentage indicate you might be overweight for your age. Consider consulting a healthcare provider for personalized guidance."
        return "Your BMI indicates you might be overweight for your age. Focus on a balanced diet and regular exercise."
    # Check for low BMI and provide nutritional advice
    elif bmi < 18.5:
        return "Your BMI is below the healthy range. Ensure you’re getting enough nutrition with calorie-dense, nutrient-rich foods."
    else:
        return "Your BMI is within a healthy range. Maintain your healthy lifestyle."

def analyze_weekly_activity(weekly_activity, strength_training_days=None):
    print(f"Debug - Weekly activity analysis: weekly_activity={weekly_activity}, strength_training_days={strength_training_days}")
    # Check for insufficient activity and recommend balanced exercise plans
    if weekly_activity < 150:
        return "It looks like you haven’t met the recommended 150 minutes of physical activity this week. Try to increase your exercise with a mix of cardio and strength training."
    # Acknowledge high activity levels and suggest further improvements
    elif weekly_activity >= 300:
        if strength_training_days and strength_training_days < 2:
            return "Excellent job on cardio! Consider adding at least 2 days of strength training to balance your fitness routine."
        return "Excellent job! You’re getting plenty of physical activity each week."
    # Encourage consistent moderate activity
    else:
        return "You're doing well; keep pushing to reach 300 minutes for optimal benefits. Include varied activities for a balanced regimen."

def analyze_aging_rate(aging_rate):
    print(f"Debug - Aging rate analysis: aging_rate={aging_rate}")
    # Check for accelerated aging and recommend targeted interventions
    if aging_rate > 1:
        return "Your pace of aging is faster than average. Prioritize anti-aging practices such as high-antioxidant foods, regular exercise, and quality sleep. Consider mindfulness practices and maintaining a balanced diet with omega-3 fatty acids."
    # Praise for healthy aging rate and encourage maintenance
    elif aging_rate < 1:
        return "Great job! Your pace of aging is below average, indicating a healthy lifestyle. Keep up with your current health practices, such as staying active and managing stress effectively."
    else:
        return "Your aging rate is typical for your age. Maintain your current habits to stay healthy, and consider periodic health check-ups to monitor any changes."

def analyze_social_interaction(social_count):
    print(f"Debug - Social interaction analysis: social_count={social_count}")
    # Recommend increasing social interactions if below threshold
    if social_count < 2:
        return "Increasing social interactions can improve mental health and overall well-being. Join community groups, volunteer, or plan weekly meetups with friends and family to foster stronger social bonds."
    # Acknowledge sufficient social interactions
    else:
        return "You have a healthy level of social interactions. Keep nurturing these connections for emotional resilience and long-term mental health."

def analyze_perception_score(perception_score):
    print(f"Debug - Perception score analysis: perception_score={perception_score}")
    # Provide recommendations if the self-reported score is low
    if perception_score < 5:
        return "Your self-reported well-being score is low. Incorporate mindfulness practices, gratitude journaling, and stress management techniques into your routine. Consider engaging in activities that bring you joy and fulfillment."
    # Acknowledge positive perception score
    else:
        return "Your perception score indicates a good mental state. Keep up the positive habits and continue practicing self-care, such as regular relaxation and maintaining a balanced work-life."

def analyze_telomere_length(telomere_length):
    print(f"Debug - Telomere length analysis: telomere_length={telomere_length}")
    # Provide advice if telomere length indicates accelerated aging
    if telomere_length < 7.0:
        return "Your telomere length is below average, indicating

def analyze_hba1c(hba1c):
    print(f"Debug - HbA1c analysis: hba1c={hba1c}")
    if hba1c >= 6.5:
        return "Your HbA1c level indicates diabetes. Immediate lifestyle changes and consultation with a healthcare provider are recommended. Implement a balanced diet with controlled carbohydrate intake."
    elif 5.7 <= hba1c < 6.5:
        return "Your HbA1c level suggests prediabetes. Focus on reducing sugar intake, regular exercise, and maintaining a healthy weight."
    else:
        return "Your HbA1c level is normal. Maintain your healthy habits and monitor regularly."

def analyze_rmr(rmr):
    print(f"Debug - RMR analysis: rmr={rmr}")
    if rmr < 1500:
        return "Your resting metabolic rate is lower than average. This might affect your energy levels and weight management. Consider consulting a nutritionist for a tailored dietary plan."
    else:
        return "Your resting metabolic rate is within a healthy range. Ensure you’re meeting your caloric needs to support your activity level."

def analyze_vo2max(vo2max):
    print(f"Debug - VO2 max analysis: vo2max={vo2


# Main function to generate recommendations
def compute_biometrics_recommendation(data):
    recommendations = []
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

    return recommendations

# Load processed data
data = pd.read_csv('../output/combined_data.csv')
recommendations = compute_biometrics_recommendation(data)

# Print recommendations and save to a file
with open('../output/recommendations.txt', 'w') as rec_outfile:
    for rec in recommendations:
        print(rec)
        rec_outfile.write(rec + '\n')

print("Recommendations generated.")
