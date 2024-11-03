import numpy as np

# Sub-function for analyzing cardiovascular health
def analyze_cardiovascular_health(score):
    print(f"Debug - Cardiovascular health score: {score}")
    if score < 50:
        return "Your cardiovascular health could be improved. Incorporate regular aerobic exercises such as jogging, swimming, or cycling to strengthen your heart."
    else:
        return "Your cardiovascular health is in a good range. Maintain regular physical activity and a heart-healthy diet."

# Sub-function for analyzing telomere length
def analyze_telomere_length(telomere_length):
    print(f"Debug - Telomere length: {telomere_length}")
    if telomere_length < 7.0:
        return "Your telomere length suggests accelerated cellular aging. Prioritize stress management, include omega-3 rich foods, and ensure sufficient sleep to support cellular health."
    else:
        return "Your telomere length is within a healthy range. Continue maintaining a balanced lifestyle with stress management and proper nutrition."

# Sub-function for analyzing metabolic health (glucose levels)
def analyze_metabolic_health(glucose_level):
    print(f"Debug - Glucose level: {glucose_level}")
    if glucose_level > 100:
        return "Your blood sugar levels indicate a need for better glucose management. Reduce refined sugars, increase dietary fiber, and engage in regular physical activity."
    else:
        return "Your glucose levels are within a healthy range. Continue with a balanced diet and regular exercise."

# Sub-function for analyzing inflammation markers
def analyze_inflammation_markers(crp_level):
    print(f"Debug - CRP level: {crp_level}")
    if crp_level > 3:
        return "High CRP levels indicate inflammation. Focus on anti-inflammatory foods like turmeric, ginger, and leafy greens. Avoid processed foods and manage stress."
    else:
        return "Your inflammation markers are within a healthy range. Maintain a diet rich in anti-inflammatory foods and keep stress levels low."

# Sub-function for hormonal balance analysis
def analyze_hormonal_balance(cortisol_level):
    print(f"Debug - Cortisol level: {cortisol_level}")
    if cortisol_level > 20:
        return "High cortisol levels indicate chronic stress. Implement stress-reduction practices like yoga, meditation, and deep breathing exercises."
    else:
        return "Your cortisol levels are balanced. Continue practicing mindfulness and stress management techniques."

# Sub-function for sleep quality analysis
def analyze_sleep_quality(sleep_hours, deep_sleep_hours):
    print(f"Debug - Sleep hours: {sleep_hours}, Deep sleep hours: {deep_sleep_hours}")
    if sleep_hours < 7 or deep_sleep_hours < 1.5:
        return "Your sleep quality could be improved. Aim for at least 7-8 hours of sleep with 1.5-2 hours of deep sleep. Prioritize a relaxing bedtime routine and reduce screen time before bed."
    else:
        return "Your sleep quality is good. Continue your current sleep hygiene practices."

# Sub-function for muscle mass and strength analysis
def analyze_muscle_mass(muscle_mass_index):
    print(f"Debug - Muscle mass index: {muscle_mass_index}")
    if muscle_mass_index < 30:
        return "Your muscle mass is below optimal levels. Incorporate strength training exercises such as weight lifting and resistance workouts."
    else:
        return "Your muscle mass is at a healthy level. Maintain regular strength training to support overall health."

# Sub-function for bone density analysis
def analyze_bone_density(bone_density_score):
    print(f"Debug - Bone density score: {bone_density_score}")
    if bone_density_score < 2.5:
        return "Your bone density indicates a risk for osteoporosis. Increase calcium and vitamin D intake and engage in weight-bearing exercises."
    else:
        return "Your bone density is within a healthy range. Continue with weight-bearing exercises and a balanced diet."

# Sub-function for immune system analysis
def analyze_immune_health(cd4_cd8_ratio):
    print(f"Debug - CD4/CD8 ratio: {cd4_cd8_ratio}")
    if cd4_cd8_ratio < 1:
        return "Your immune system shows signs of potential imbalance. Consider immune-boosting practices like a nutrient-rich diet, moderate exercise, and adequate sleep."
    else:
        return "Your immune system appears balanced. Maintain a healthy diet, regular exercise, and proper rest."

# Sub-function for hydration analysis
def analyze_hydration(hydration_level):
    print(f"Debug - Hydration level: {hydration_level}")
    if hydration_level < 50:
        return "You are not adequately hydrated. Increase your daily water intake to improve cellular function and overall health."
    else:
        return "Your hydration level is sufficient. Keep up the good hydration habits."

# Sub-function for oxidative stress analysis
def analyze_oxidative_stress(antioxidant_levels):
    print(f"Debug - Antioxidant levels: {antioxidant_levels}")
    if antioxidant_levels < 1:
        return "Your antioxidant levels are low, indicating potential oxidative stress. Increase intake of antioxidant-rich foods such as berries, dark chocolate, and green tea."
    else:
        return "Your antioxidant levels are healthy. Maintain a diet rich in fruits and vegetables."

# Sub-function for metabolic rate analysis
def analyze_metabolic_rate(rmr):
    print(f"Debug - Resting Metabolic Rate (RMR): {rmr}")
    if rmr < 1500:
        return "Your metabolic rate is lower than average. Consider consulting a nutritionist to adjust your diet and incorporate metabolic-boosting exercises."
    else:
        return "Your metabolic rate is within a healthy range. Continue your current diet and exercise routine."

# Sub-function for analyzing skin health (collagen levels)
def analyze_skin_health(collagen_level):
    print(f"Debug - Collagen level: {collagen_level}")
    if collagen_level < 3:
        return "Low collagen levels may impact skin elasticity. Include collagen-rich foods and consider supplements. Protect your skin from excessive sun exposure."
    else:
        return "Your collagen levels are healthy. Maintain a diet rich in vitamin C and amino acids."

# Sub-function for liver function analysis (ALT levels)
def analyze_liver_function(alt_level):
    print(f"Debug - ALT level: {alt_level}")
    if alt_level > 35:
        return "Elevated ALT levels indicate potential liver stress. Reduce alcohol consumption and consider a liver-supportive diet with leafy greens and antioxidant-rich foods."
    else:
        return "Your liver function appears healthy. Continue with a balanced diet and moderate alcohol intake."

# Sub-function for kidney function analysis (creatinine levels)
def analyze_kidney_function(creatinine_level):
    print(f"Debug - Creatinine level: {creatinine_level}")
    if creatinine_level > 1.2:
        return "High creatinine levels may indicate kidney stress. Stay hydrated and consider reducing high-protein intake if advised by a healthcare provider."
    else:
        return "Your kidney function is within normal range. Maintain proper hydration and a balanced diet."

# Sub-function for cholesterol analysis (LDL levels)
def analyze_cholesterol(ldl_level):
    print(f"Debug - LDL level: {ldl_level}")
    if ldl_level > 130:
        return "High LDL cholesterol levels may increase cardiovascular risk. Consider dietary changes to reduce saturated fat and include more fiber-rich foods."
    else:
        return "Your LDL cholesterol is within a healthy range. Maintain heart-healthy eating habits."

# Sub-function for blood pressure analysis
def analyze_blood_pressure(systolic, diastolic):
    print(f"Debug - Blood pressure: Systolic={systolic}, Diastolic={diastolic}")
    if systolic > 130 or diastolic > 80:
        return "Elevated blood pressure detected. Monitor your sodium intake, maintain regular exercise, and manage stress."
    else:
        return "Your blood pressure is within a healthy range. Continue your current lifestyle habits."

# Sub-function for gut health analysis (gut microbiome diversity)
def analyze_gut_health(microbiome_score):
    print(f"Debug - Gut microbiome score: {microbiome_score}")
    if microbiome_score < 5:
        return "Your gut microbiome diversity is low. Increase fiber intake, consume fermented foods like yogurt and kimchi, and consider prebiotic supplements."
    else:
        return "Your gut health is in good condition. Maintain a diverse diet to support microbiome balance."

# Sub-function for joint health analysis (inflammation markers)
def analyze_joint_health(joint_inflammation_marker):
    print(f"Debug - Joint inflammation marker: {joint_in


# Sub-function for analyzing cardiovascular health
def analyze_cardiovascular_health(score):
    print(f"Debug - Cardiovascular health score: {score}")
    if score < 50:
        return "Your cardiovascular health could be improved. Incorporate regular aerobic exercises such as jogging, swimming, or cycling to strengthen your heart."
    else:
        return "Your cardiovascular health is in a good range. Maintain regular physical activity and a heart-healthy diet."

# Sub-function for analyzing telomere length
def analyze_telomere_length(telomere_length):
    print(f"Debug - Telomere length: {telomere_length}")
    if telomere_length < 7.0:
        return "Your telomere length suggests accelerated cellular aging. Prioritize stress management, include omega-3 rich foods, and ensure sufficient sleep to support cellular health."
    else:
        return "Your telomere length is within a healthy range. Continue maintaining a balanced lifestyle with stress management and proper nutrition."

# Sub-function for analyzing metabolic health (glucose levels)
def analyze_metabolic_health(glucose_level):
    print(f"Debug - Glucose level: {glucose_level}")
    if glucose_level > 100:
        return "Your blood sugar levels indicate a need for better glucose management. Reduce refined sugars, increase dietary fiber, and engage in regular physical activity."
    else:
        return "Your glucose levels are within a healthy range. Continue with a balanced diet and regular exercise."

# Sub-function for analyzing inflammation markers
def analyze_inflammation_markers(crp_level):
    print(f"Debug - CRP level: {crp_level}")
    if crp_level > 3:
        return "High CRP levels indicate inflammation. Focus on anti-inflammatory foods like turmeric, ginger, and leafy greens. Avoid processed foods and manage stress."
    else:
        return "Your inflammation markers are within a healthy range. Maintain a diet rich in anti-inflammatory foods and keep stress levels low."

# Sub-function for hormonal balance analysis
def analyze_hormonal_balance(cortisol_level):
    print(f"Debug - Cortisol level: {cortisol_level}")
    if cortisol_level > 20:
        return "High cortisol levels indicate chronic stress. Implement stress-reduction practices like yoga, meditation, and deep breathing exercises."
    else:
        return "Your cortisol levels are balanced. Continue practicing mindfulness and stress management techniques."

# Sub-function for sleep quality analysis
def analyze_sleep_quality(sleep_hours, deep_sleep_hours):
    print(f"Debug - Sleep hours: {sleep_hours}, Deep sleep hours: {deep_sleep_hours}")
    if sleep_hours < 7 or deep_sleep_hours < 1.5:
        return "Your sleep quality could be improved. Aim for at least 7-8 hours of sleep with 1.5-2 hours of deep sleep. Prioritize a relaxing bedtime routine and reduce screen time before bed."
    else:
        return "Your sleep quality is good. Continue your current sleep hygiene practices."

# Sub-function for muscle mass and strength analysis
def analyze_muscle_mass(muscle_mass_index):
    print(f"Debug - Muscle mass index: {muscle_mass_index}")
    if muscle_mass_index < 30:
        return "Your muscle mass is below optimal levels. Incorporate strength training exercises such as weight lifting and resistance workouts."
    else:
        return "Your muscle mass is at a healthy level. Maintain regular strength training to support overall health."

# Sub-function for bone density analysis
def analyze_bone_density(bone_density_score):
    print(f"Debug - Bone density score: {bone_density_score}")
    if bone_density_score < 2.5:
        return "Your bone density indicates a risk for osteoporosis. Increase calcium and vitamin D intake and engage in weight-bearing exercises."
    else:
        return "Your bone density is within a healthy range. Continue with weight-bearing exercises and a balanced diet."

# Sub-function for immune system analysis
def analyze_immune_health(cd4_cd8_ratio):
    print(f"Debug - CD4/CD8 ratio: {cd4_cd8_ratio}")
    if cd4_cd8_ratio < 1:
        return "Your immune system shows signs of potential imbalance. Consider immune-boosting practices like a nutrient-rich diet, moderate exercise, and adequate sleep."
    else:
        return "Your immune system appears balanced. Maintain a healthy diet, regular exercise, and proper rest."

# Sub-function for hydration analysis
def analyze_hydration(hydration_level):
    print(f"Debug - Hydration level: {hydration_level}")
    if hydration_level < 50:
        return "You are not adequately hydrated. Increase your daily water intake to improve cellular function and overall health."
    else:
        return "Your hydration level is sufficient. Keep up the good hydration habits."

# Sub-function for oxidative stress analysis
def analyze_oxidative_stress(antioxidant_levels):
    print(f"Debug - Antioxidant levels: {antioxidant_levels}")
    if antioxidant_levels < 1:
        return "Your antioxidant levels are low, indicating potential oxidative stress. Increase intake of antioxidant-rich foods such as berries, dark chocolate, and green tea."
    else:
        return "Your antioxidant levels are healthy. Maintain a diet rich in fruits and vegetables."

# Sub-function for metabolic rate analysis
def analyze_metabolic_rate(rmr):
    print(f"Debug - Resting Metabolic Rate (RMR): {rmr}")
    if rmr < 1500:
        return "Your metabolic rate is lower than average. Consider consulting a nutritionist to adjust your diet and incorporate metabolic-boosting exercises."
    else:
        return "Your metabolic rate is within a healthy range. Continue your current diet and exercise routine."
import numpy as np

# Sub-function for analyzing cardiovascular health
def analyze_cardiovascular_health(score):
    print(f"Debug - Cardiovascular health score: {score}")
    if score < 50:
        return "Your cardiovascular health could be improved. Incorporate regular aerobic exercises such as jogging, swimming, or cycling to strengthen your heart."
    else:
        return "Your cardiovascular health is in a good range. Maintain regular physical activity and a heart-healthy diet."

# Sub-function for analyzing telomere length
def analyze_telomere_length(telomere_length):
    print(f"Debug - Telomere length: {telomere_length}")
    if telomere_length < 7.0:
        return "Your telomere length suggests accelerated cellular aging. Prioritize stress management, include omega-3 rich foods, and ensure sufficient sleep to support cellular health."
    else:
        return "Your telomere length is within a healthy range. Continue maintaining a balanced lifestyle with stress management and proper nutrition."

# Sub-function for analyzing metabolic health (glucose levels)
def analyze_metabolic_health(glucose_level):
    print(f"Debug - Glucose level: {glucose_level}")
    if glucose_level > 100:
        return "Your blood sugar levels indicate a need for better glucose management. Reduce refined sugars, increase dietary fiber, and engage in regular physical activity."
    else:
        return "Your glucose levels are within a healthy range. Continue with a balanced diet and regular exercise."

# Sub-function for analyzing inflammation markers
def analyze_inflammation_markers(crp_level):
    print(f"Debug - CRP level: {crp_level}")
    if crp_level > 3:
        return "High CRP levels indicate inflammation. Focus on anti-inflammatory foods like turmeric, ginger, and leafy greens. Avoid processed foods and manage stress."
    else:
        return "Your inflammation markers are within a healthy range. Maintain a diet rich in anti-inflammatory foods and keep stress levels low."

# Sub-function for hormonal balance analysis
def analyze_hormonal_balance(cortisol_level):
    print(f"Debug - Cortisol level: {cortisol_level}")
    if cortisol_level > 20:
        return "High cortisol levels indicate chronic stress. Implement stress-reduction practices like yoga, meditation, and deep breathing exercises."
    else:
        return "Your cortisol levels are balanced. Continue practicing mindfulness and stress management techniques."

# Sub-function for sleep quality analysis
def analyze_sleep_quality(sleep_hours, deep_sleep_hours):
    print(f"Debug - Sleep hours: {sleep_hours}, Deep sleep hours: {deep_sleep_hours}")
    if sleep_hours < 7 or deep_sleep_hours < 1.5:
        return "Your sleep quality could be improved. Aim for at least 7-8 hours of sleep with 1.5-2 hours of deep sleep. Prioritize a relaxing bedtime routine and reduce screen time before bed."
    else:
        return "Your sleep quality is good. Continue your current sleep hygiene practices."

# Sub-function for muscle mass and strength analysis
def analyze_muscle_mass(muscle_mass_index):
    print(f"Debug - Muscle mass index: {muscle_mass_index}")
    if muscle_mass_index < 30:
        return "Your muscle mass is below optimal levels. Incorporate strength training exercises such as weight lifting and resistance workouts."
    else:
        return "Your muscle mass is at a healthy level. Maintain regular strength training to support overall health."

# Sub-function for bone density analysis
def analyze_bone_density(bone_density_score):
    print(f"Debug - Bone density score: {bone_density_score}")
    if bone_density_score < 2.5:
        return "Your bone density indicates a risk for osteoporosis. Increase calcium and vitamin D intake and engage in weight-bearing exercises."
    else:
        return "Your bone density is within a healthy range. Continue with weight-bearing exercises and a balanced diet."

# Sub-function for immune system analysis
def analyze_immune_health(cd4_cd8_ratio):
    print(f"Debug - CD4/CD8 ratio: {cd4_cd8_ratio}")
    if cd4_cd8_ratio < 1:
        return "Your immune system shows signs of potential imbalance. Consider immune-boosting practices like a nutrient-rich diet, moderate exercise, and adequate sleep."
    else:
        return "Your immune system appears balanced. Maintain a healthy diet, regular exercise, and proper rest."

# Sub-function for hydration analysis
def analyze_hydration(hydration_level):
    print(f"Debug - Hydration level: {hydration_level}")
    if hydration_level < 50:
        return "You are not adequately hydrated. Increase your daily water intake to improve cellular function and overall health."
    else:
        return "Your hydration level is sufficient. Keep up the good hydration habits."

# Sub-function for oxidative stress analysis
def analyze_oxidative_stress(antioxidant_levels):
    print(f"Debug - Antioxidant levels: {antioxidant_levels}")
    if antioxidant_levels < 1:
        return "Your antioxidant levels are low, indicating potential oxidative stress. Increase intake of antioxidant-rich foods such as berries, dark chocolate, and green tea."
    else:
        return "Your antioxidant levels are healthy. Maintain a diet rich in fruits and vegetables."

# Sub-function for metabolic rate analysis
def analyze_metabolic_rate(rmr):
    print(f"Debug - Resting Metabolic Rate (RMR): {rmr}")
    if rmr < 1500:
        return "Your metabolic rate is lower than average. Consider consulting a nutritionist to adjust your diet and incorporate metabolic-boosting exercises."
    else:
        return "Your metabolic rate is within a healthy range. Continue your current diet and exercise routine."

# Sub-function for analyzing skin health (collagen levels)
def analyze_skin_health(collagen_level):
    print(f"Debug - Collagen level: {collagen_level}")
    if collagen_level < 3:
        return "Low collagen levels may impact skin elasticity. Include collagen-rich foods and consider supplements. Protect your skin from excessive sun exposure."
    else:
        return "Your collagen levels are healthy. Maintain a diet rich in vitamin C and amino acids."

# Sub-function for liver function analysis (ALT levels)
def analyze_liver_function(alt_level):
    print(f"Debug - ALT level: {alt_level}")
    if alt_level > 35:
        return "Elevated ALT levels indicate potential liver stress. Reduce alcohol consumption and consider a liver-supportive diet with leafy greens and antioxidant-rich foods."
    else:
        return "Your liver function appears healthy. Continue with a balanced diet and moderate alcohol intake."

# Sub-function for kidney function analysis (creatinine levels)
def analyze_kidney_function(creatinine_level):
    print(f"Debug - Creatinine level: {creatinine_level}")
    if creatinine_level > 1.2:
        return "High creatinine levels may indicate kidney stress. Stay hydrated and consider reducing high-protein intake if advised by a healthcare provider."
    else:
        return "Your kidney function is within normal range. Maintain proper hydration and a balanced diet."

# Sub-function for cholesterol analysis (LDL levels)
def analyze_cholesterol(ldl_level):
    print(f"Debug - LDL level: {ldl_level}")
    if ldl_level > 130:
        return "High LDL cholesterol levels may increase cardiovascular risk. Consider dietary changes to reduce saturated fat and include more fiber-rich foods."
    else:
        return "Your LDL cholesterol is within a healthy range. Maintain heart-healthy eating habits."

# Sub-function for blood pressure analysis
def analyze_blood_pressure(systolic, diastolic):
    print(f"Debug - Blood pressure: Systolic={systolic}, Diastolic={diastolic}")
    if systolic > 130 or diastolic > 80:
        return "Elevated blood pressure detected. Monitor your sodium intake, maintain regular exercise, and manage stress."
    else:
        return "Your blood pressure is within a healthy range. Continue your current lifestyle habits."

# Sub-function for gut health analysis (gut microbiome diversity)
def analyze_gut_health(microbiome_score):
    print(f"Debug - Gut microbiome score: {microbiome_score}")
    if microbiome_score < 5:
        return "Your gut microbiome diversity is low. Increase fiber intake, consume fermented foods like yogurt and kimchi, and consider prebiotic supplements."
    else:
        return "Your gut health is in good condition. Maintain a diverse diet to support microbiome balance."

# Sub-function for joint health analysis (inflammation markers)
def analyze_joint_health(joint_inflammation_marker):
    print(f"Debug - Joint inflammation marker: {joint_in

# Main function to analyze aging rate and aggregate recommendations
def analyze_aging_rate(aging_rate, cardiovascular_health=None, telomere_length=None, metabolic_factors=None, crp_level=None, cortisol_level=None, sleep_hours=None, deep_sleep_hours=None, muscle_mass_index=None, bone_density_score=None, cd4_cd8_ratio=None, hydration_level=None, antioxidant_levels=None, rmr=None):
    print(f"Debug - Comprehensive aging rate analysis")
    recommendations = []

    if aging_rate > 1:
        recommendations.append("Your pace of aging is faster than average. Prioritize comprehensive anti-aging practices.")
        recommendations.append(analyze_cardiovascular_health(cardiovascular_health))
        recommendations.append(analyze_telomere_length(telomere_length))
        recommendations.append(analyze_metabolic_health(metabolic_factors.get('glucose') if metabolic_factors else None))
        recommendations.append(analyze_inflammation_markers(crp_level))
        recommendations.append(analyze_hormonal_balance(cortisol_level))
        recommendations.append(analyze_sleep_quality(sleep_hours, deep_sleep_hours))
        recommendations.append(analyze_muscle_mass(muscle_mass_index))
        recommendations.append(analyze_bone_density(bone_density_score))
        recommendations.append(analyze_immune_health(cd4_cd8_ratio))
        recommendations.append(analyze_hydration(hydration_level))
        recommendations.append(analyze_oxidative_stress(antioxidant_levels))
        recommendations.append(analyze_metabolic_rate(rmr))
    elif aging_rate < 1:
        recommendations.append(
            "Great job! Your pace of aging is below average. Maintain current health practices, including balanced nutrition and regular exercise."
        )
    else:
        recommendations.append(
            "Your aging rate is typical. Continue healthy habits and consider periodic health assessments to catch changes early."
        )

    return " ".join([rec for rec in recommendations if rec])

# Example usage:
# result = analyze_aging_rate(1.2, cardiovascular_health=45, telomere_length=6.5, metabolic_factors={'glucose': 110}, crp_level=4, cortisol_level=22, sleep_hours=6, deep_sleep_hours=1.2, muscle_mass_index=28, bone_density_score=2.3, cd4_cd8_ratio=0.9, hydration_level=45, antioxidant_levels=0.8, rmr=1400)
# print(result)
