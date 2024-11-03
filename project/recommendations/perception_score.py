# Expanded perception score analysis incorporating various user data points

def analyze_perception_score(perception_score, stress_level=None, mindfulness_practices=None, body_image=None, personality_type=None, sentiment_data=None, instagram_data=None):
    print(f"Debug - Perception score analysis: perception_score={perception_score}, stress_level={stress_level}, mindfulness_practices={mindfulness_practices}, body_image={body_image}, personality_type={personality_type}, sentiment_data={sentiment_data}, instagram_data={instagram_data}")

    # Provide comprehensive recommendations if the perception score is low
    if perception_score < 5:
        advice = [
            "Your self-reported well-being score is low. Incorporate activities like mindfulness practices, journaling, or guided meditations to improve your mental state.",
            "Engage in physical activities like yoga or moderate exercise, as they can boost mood and reduce stress levels."
        ]
        if stress_level and stress_level > 7:
            advice.append("Your stress levels are high. Prioritize stress reduction techniques such as deep breathing exercises, progressive muscle relaxation, or talking to a mental health professional.")
        if not mindfulness_practices:
            advice.append("Consider starting mindfulness routines, like daily meditation or gratitude journaling, to enhance emotional resilience.")
        if body_image:
            advice.append(analyze_body_image(body_image))
        if personality_type:
            advice.append(analyze_personality_type(personality_type))
        if sentiment_data:
            advice.append(analyze_sentiment_over_time(sentiment_data))
        if instagram_data:
            advice.append(analyze_instagram_hobbies(interests=instagram_data))
        return " ".join(advice)

    # Acknowledge positive perception score and provide encouragement
    else:
        feedback = [
            "Your perception score indicates a good mental state. Keep up with the habits that are contributing to your well-being.",
            "Continuing to engage in self-care routines, balanced work-life practices, and physical activity will help sustain your positive outlook."
        ]
        if mindfulness_practices:
            feedback.append("It’s great that you practice mindfulness regularly. Keep incorporating these practices to maintain emotional balance.")
        return " ".join(feedback)

# Sub-function for analyzing body image from a photo
def analyze_body_image(photo_analysis_result):
    print(f"Debug - Body image analysis result: {photo_analysis_result}")
    if photo_analysis_result['BMI'] > 25:
        return "Your body analysis indicates a higher BMI. Consider a balanced diet and regular exercise to maintain optimal health."
    else:
        return "Your body analysis shows a healthy BMI. Keep maintaining your current lifestyle."

# Sub-function for analyzing personality type
from sklearn.metrics import pairwise_distances

def analyze_personality_type(personality_type):
    print(f"Debug - Personality type: {personality_type}")
    recommendations = {
        'INTJ': "Leverage your strategic thinking by planning regular mental breaks to avoid burnout.",
        'ESFP': "Channel your energy into group activities that promote both social interaction and physical well-being.",
        'INFJ': "Balance your introspective nature with activities that encourage physical activity, such as dance or martial arts.",
        'ENTP': "Keep a varied routine to avoid stagnation and ensure you stay engaged mentally and physically."
    }
    return recommendations.get(personality_type, "Maintain self-reflection and balance your activities to support your well-being.")

# Sub-function for sentiment analysis over time
def analyze_sentiment_over_time(sentiment_data):
    print(f"Debug - Sentiment data analysis: {sentiment_data}")
    avg_sentiment = np.mean(sentiment_data)
    if avg_sentiment < 0:
        return "Your message history indicates overall negative sentiment. Consider reaching out for social support or engaging in positive conversations."
    else:
        return "Your messages reflect positive sentiment. Keep maintaining a positive communication style."

# Sub-function for analyzing Instagram hobbies and interests
def analyze_instagram_hobbies(interests):
    print(f"Debug - Instagram analysis: {interests}")
    if 'outdoor' in interests:
        return "Your interest in outdoor activities suggests a love for nature. Make time for hiking or nature walks to enhance mental well-being."
    elif 'art' in interests:
        return "Artistic hobbies indicate creativity. Consider engaging in painting or crafts to relax and inspire."
    else:
        return "Your hobbies are diverse. Continue pursuing activities that bring you joy and balance."

# Additional sub-functions for a holistic approach

def analyze_sleep_patterns(sleep_data):
    print(f"Debug - Sleep data: {sleep_data}")
    if sleep_data['consistency'] < 80:
        return "Your sleep pattern shows inconsistencies. Aim for a regular sleep schedule to boost overall mood and perception."
    return "Your sleep patterns are consistent. Keep it up!"

def analyze_diet_nutrition(diet_score):
    print(f"Debug - Diet score: {diet_score}")
    if diet_score < 60:
        return "Your nutrition score is below optimal. Incorporate more whole foods, fruits, and vegetables for better health."
    return "Your diet supports your health. Maintain your balanced meals."

def analyze_physical_activity(activity_level):
    print(f"Debug - Activity level: {activity_level}")
    if activity_level < 3:
        return "Your activity level is low. Increase physical movement through activities you enjoy like walking or cycling."
    return "Your physical activity is sufficient. Keep moving!"

def analyze_hydration_habits(hydration_score):
    print(f"Debug - Hydration score: {hydration_score}")
    if hydration_score < 50:
        return "Hydration is key to maintaining mood and energy. Ensure you drink enough water throughout the day."
    return "Your hydration habits are on point. Stay hydrated!"

def analyze_financial_stress(financial_stress_score):
    print(f"Debug - Financial stress score: {financial_stress_score}")
    if financial_stress_score > 70:
        return "Financial stress can impact overall perception and mental health. Consider financial planning or counseling for support."
    return "Your financial stress is under control. Keep managing your finances wisely."

def analyze_social_connections(social_network_strength):
    print(f"Debug - Social network strength: {social_network_strength}")
    if social_network_strength < 5:
        return "Strengthen your social connections. Regular interactions with close friends and family can improve your perception and happiness."
    return "Your social network is strong. Maintain those relationships."

def analyze_work_life_balance(work_life_score):
    print(f"Debug - Work-life balance score: {work_life_score}")
    if work_life_score < 50:
        return "Your work-life balance could be improved. Allocate time for relaxation and hobbies outside of work."
    return "Your work-life balance is good. Keep nurturing time for personal well-being."

def analyze_self_esteem(self_esteem_score):
    print(f"Debug - Self-esteem score: {self_esteem_score}")
    if self_esteem_score < 40:
        return "Your self-esteem could use a boost. Practice positive affirmations and set achievable goals to build confidence."
    return "Your self-esteem is healthy. Continue with positive self-talk and achieving personal goals."

def analyze_emotional_resilience(resilience_score):
    print(f"Debug - Emotional resilience score: {resilience_score}")
    if resilience_score < 30:
        return "Building emotional resilience can help with challenges. Engage in practices that build coping skills, like mindfulness and reflection."
    return "Your emotional resilience is strong. Maintain these habits to handle stress effectively."

# Main function to analyze perception and compile advice
def compile_perception_analysis(perception_score, **kwargs):
    print(f"Debug - Starting comprehensive perception analysis")
    results = []
    results.append(analyze_perception_score(perception_score, kwargs.get('stress_level'), kwargs.get('mindfulness_practices'), kwargs.get('body_image'), kwargs.get('personality_type'), kwargs.get('sentiment_data'), kwargs.get('instagram_data')))
    results.append(analyze_sleep_patterns(kwargs.get('sleep_data', {})))
    results.append(analyze_diet_nutrition(kwargs.get('diet_score', 70)))
    results.append(analyze_physical_activity(kwargs.get('activity_level', 5)))
    results.append(analyze_hydration_habits(kwargs.get('hydration_score', 60)))
    results.append(analyze_financial_stress(kwargs.get('financial_stress_score', 40)))
    results.append(analyze_social_connections(kwargs.get('social_network_strength', 7)))
    results.append(analyze_work_life_balance(kwargs.get('work_life_score', 70)))









-------







# Expanded perception score analysis incorporating various user data points

def analyze_perception_score(perception_score, stress_level=None, mindfulness_practices=None, body_image=None, personality_type=None, sentiment_data=None, instagram_data=None):
    print(f"Debug - Perception score analysis: perception_score={perception_score}, stress_level={stress_level}, mindfulness_practices={mindfulness_practices}, body_image={body_image}, personality_type={personality_type}, sentiment_data={sentiment_data}, instagram_data={instagram_data}")

    # Provide comprehensive recommendations if the perception score is low
    if perception_score < 5:
        advice = [
            "Your self-reported well-being score is low. Incorporate activities like mindfulness practices, journaling, or guided meditations to improve your mental state.",
            "Engage in physical activities like yoga or moderate exercise, as they can boost mood and reduce stress levels."
        ]
        if stress_level and stress_level > 7:
            advice.append("Your stress levels are high. Prioritize stress reduction techniques such as deep breathing exercises, progressive muscle relaxation, or talking to a mental health professional.")
        if not mindfulness_practices:
            advice.append("Consider starting mindfulness routines, like daily meditation or gratitude journaling, to enhance emotional resilience.")
        if body_image:
            advice.append(analyze_body_image(body_image))
        if personality_type:
            advice.append(analyze_personality_type(personality_type))
        if sentiment_data:
            advice.append(analyze_sentiment_over_time(sentiment_data))
        if instagram_data:
            advice.append(analyze_instagram_hobbies(interests=instagram_data))
        return " ".join(advice)

    # Acknowledge positive perception score and provide encouragement
    else:
        feedback = [
            "Your perception score indicates a good mental state. Keep up with the habits that are contributing to your well-being.",
            "Continuing to engage in self-care routines, balanced work-life practices, and physical activity will help sustain your positive outlook."
        ]
        if mindfulness_practices:
            feedback.append("It’s great that you practice mindfulness regularly. Keep incorporating these practices to maintain emotional balance.")
        return " ".join(feedback)

# Sub-function for analyzing body image from a photo
def analyze_body_image(photo_analysis_result):
    print(f"Debug - Body image analysis result: {photo_analysis_result}")
    if photo_analysis_result['BMI'] > 25:
        return "Your body analysis indicates a higher BMI. Consider a balanced diet and regular exercise to maintain optimal health."
    else:
        return "Your body analysis shows a healthy BMI. Keep maintaining your current lifestyle."

# Sub-function for analyzing personality type
from sklearn.metrics import pairwise_distances

def analyze_personality_type(personality_type):
    print(f"Debug - Personality type: {personality_type}")
    recommendations = {
        'INTJ': "Leverage your strategic thinking by planning regular mental breaks to avoid burnout.",
        'ESFP': "Channel your energy into group activities that promote both social interaction and physical well-being.",
        'INFJ': "Balance your introspective nature with activities that encourage physical activity, such as dance or martial arts.",
        'ENTP': "Keep a varied routine to avoid stagnation and ensure you stay engaged mentally and physically."
    }
    return recommendations.get(personality_type, "Maintain self-reflection and balance your activities to support your well-being.")

# Sub-function for sentiment analysis over time
def analyze_sentiment_over_time(sentiment_data):
    print(f"Debug - Sentiment data analysis: {sentiment_data}")
    avg_sentiment = np.mean(sentiment_data)
    if avg_sentiment < 0:
        return "Your message history indicates overall negative sentiment. Consider reaching out for social support or engaging in positive conversations."
    else:
        return "Your messages reflect positive sentiment. Keep maintaining a positive communication style."

# Sub-function for analyzing Instagram hobbies and interests
def analyze_instagram_hobbies(interests):
    print(f"Debug - Instagram analysis: {interests}")
    if 'outdoor' in interests:
        return "Your interest in outdoor activities suggests a love for nature. Make time for hiking or nature walks to enhance mental well-being."
    elif 'art' in interests:
        return "Artistic hobbies indicate creativity. Consider engaging in painting or crafts to relax and inspire."
    else:
        return "Your hobbies are diverse. Continue pursuing activities that bring you joy and balance."

# Additional sub-functions for a holistic approach

def analyze_sleep_patterns(sleep_data):
    print(f"Debug - Sleep data: {sleep_data}")
    if sleep_data['consistency'] < 80:
        return "Your sleep pattern shows inconsistencies. Aim for a regular sleep schedule to boost overall mood and perception."
    return "Your sleep patterns are consistent. Keep it up!"

def analyze_diet_nutrition(diet_score):
    print(f"Debug - Diet score: {diet_score}")
    if diet_score < 60:
        return "Your nutrition score is below optimal. Incorporate more whole foods, fruits, and vegetables for better health."
    return "Your diet supports your health. Maintain your balanced meals."

def analyze_physical_activity(activity_level):
    print(f"Debug - Activity level: {activity_level}")
    if activity_level < 3:
        return "Your activity level is low. Increase physical movement through activities you enjoy like walking or cycling."
    return "Your physical activity is sufficient. Keep moving!"

def analyze_hydration_habits(hydration_score):
    print(f"Debug - Hydration score: {hydration_score}")
    if hydration_score < 50:
        return "Hydration is key to maintaining mood and energy. Ensure you drink enough water throughout the day."
    return "Your hydration habits are on point. Stay hydrated!"

def analyze_financial_stress(financial_stress_score):
    print(f"Debug - Financial stress score: {financial_stress_score}")
    if financial_stress_score > 70:
        return "Financial stress can impact overall perception and mental health. Consider financial planning or counseling for support."
    return "Your financial stress is under control. Keep managing your finances wisely."

def analyze_social_connections(social_network_strength):
    print(f"Debug - Social network strength: {social_network_strength}")
    if social_network_strength < 5:
        return "Strengthen your social connections. Regular interactions with close friends and family can improve your perception and happiness."
    return "Your social network is strong. Maintain those relationships."

def analyze_work_life_balance(work_life_score):
    print(f"Debug - Work-life balance score: {work_life_score}")
    if work_life_score < 50:
        return "Your work-life balance could be improved. Allocate time for relaxation and hobbies outside of work."
    return "Your work-life balance is good. Keep nurturing time for personal well-being."

def analyze_self_esteem(self_esteem_score):
    print(f"Debug - Self-esteem score: {self_esteem_score}")
    if self_esteem_score < 40:
        return "Your self-esteem could use a boost. Practice positive affirmations and set achievable goals to build confidence."
    return "Your self-esteem is healthy. Continue with positive self-talk and achieving personal goals."

def analyze_emotional_resilience(resilience_score):
    print(f"Debug - Emotional resilience score: {resilience_score}")
    if resilience_score < 30:
        return "Building emotional resilience can help with challenges. Engage in practices that build coping skills, like mindfulness and reflection."
    return "Your emotional resilience is strong. Maintain these habits to handle stress effectively."

# Main function to analyze perception and compile advice
def compile_perception_analysis(perception_score, **kwargs):
    print(f"Debug - Starting comprehensive perception analysis")
    results = []
    results.append(analyze_perception_score(perception_score, kwargs.get('stress_level'), kwargs.get('mindfulness_practices'), kwargs.get('body_image'), kwargs.get('personality_type'), kwargs.get('sentiment_data'), kwargs.get('instagram_data')))
    results.append(analyze_sleep_patterns(kwargs.get('sleep_data', {})))
    results.append(analyze_diet_nutrition(kwargs.get('diet_score', 70)))
    results.append(analyze_physical_activity(kwargs.get('activity_level', 5)))
    results.append(analyze_hydration_habits(kwargs.get('hydration_score', 60)))
    results.append(analyze_financial_stress(kwargs.get('financial_stress_score', 40)))
    results.append(analyze_social_connections(kwargs.get('social_network_strength', 7)))
    results.append(analyze_work_life_balance(kwargs.get('work_life_score', 70)))

# Expanded perception score analysis incorporating various user data points

def analyze_perception_score(perception_score, stress_level=None, mindfulness_practices=None, body_image=None, personality_type=None, sentiment_data=None, instagram_data=None):
    print(f"Debug - Perception score analysis: perception_score={perception_score}, stress_level={stress_level}, mindfulness_practices={mindfulness_practices}, body_image={body_image}, personality_type={personality_type}, sentiment_data={sentiment_data}, instagram_data={instagram_data}")

    # Provide comprehensive recommendations if the perception score is low
    if perception_score < 5:
        advice = [
            "Your self-reported well-being score is low. Incorporate activities like mindfulness practices, journaling, or guided meditations to improve your mental state.",
            "Engage in physical activities like yoga or moderate exercise, as they can boost mood and reduce stress levels."
        ]
        if stress_level and stress_level > 7:
            advice.append("Your stress levels are high. Prioritize stress reduction techniques such as deep breathing exercises, progressive muscle relaxation, or talking to a mental health professional.")
        if not mindfulness_practices:
            advice.append("Consider starting mindfulness routines, like daily meditation or gratitude journaling, to enhance emotional resilience.")
        if body_image:
            advice.append(analyze_body_image(body_image))
        if personality_type:
            advice.append(analyze_personality_type(personality_type))
        if sentiment_data:
            advice.append(analyze_sentiment_over_time(sentiment_data))
        if instagram_data:
            advice.append(analyze_instagram_hobbies(interests=instagram_data))
        return " ".join(advice)

    # Acknowledge positive perception score and provide encouragement
    else:
        feedback = [
            "Your perception score indicates a good mental state. Keep up with the habits that are contributing to your well-being.",
            "Continuing to engage in self-care routines, balanced work-life practices, and physical activity will help sustain your positive outlook."
        ]
        if mindfulness_practices:
            feedback.append("It’s great that you practice mindfulness regularly. Keep incorporating these practices to maintain emotional balance.")
        return " ".join(feedback)

# Sub-function for analyzing body image from a photo
def analyze_body_image(photo_analysis_result):
    print(f"Debug - Body image analysis result: {photo_analysis_result}")
    if photo_analysis_result['BMI'] > 25:
        return "Your body analysis indicates a higher BMI. Consider a balanced diet and regular exercise to maintain optimal health."
    else:
        return "Your body analysis shows a healthy BMI. Keep maintaining your current lifestyle."

# Sub-function for analyzing personality type
from sklearn.metrics import pairwise_distances

def analyze_personality_type(personality_type):
    print(f"Debug - Personality type: {personality_type}")
    recommendations = {
        'INTJ': "Leverage your strategic thinking by planning regular mental breaks to avoid burnout.",
        'ESFP': "Channel your energy into group activities that promote both social interaction and physical well-being.",
        'INFJ': "Balance your introspective nature with activities that encourage physical activity, such as dance or martial arts.",
        'ENTP': "Keep a varied routine to avoid stagnation and ensure you stay engaged mentally and physically."
    }
    return recommendations.get(personality_type, "Maintain self-reflection and balance your activities to support your well-being.")

# Sub-function for sentiment analysis over time
def analyze_sentiment_over_time(sentiment_data):
    print(f"Debug - Sentiment data analysis: {sentiment_data}")
    avg_sentiment = np.mean(sentiment_data)
    if avg_sentiment < 0:
        return "Your message history indicates overall negative sentiment. Consider reaching out for social support or engaging in positive conversations."
    else:
        return "Your messages reflect positive sentiment. Keep maintaining a positive communication style."

# Sub-function for analyzing Instagram hobbies and interests
def analyze_instagram_hobbies(interests):
    print(f"Debug - Instagram analysis: {interests}")
    if 'outdoor' in interests:
        return "Your interest in outdoor activities suggests a love for nature. Make time for hiking or nature walks to enhance mental well-being."
    elif 'art' in interests:
        return "Artistic hobbies indicate creativity. Consider engaging in painting or crafts to relax and inspire."
    else:
        return "Your hobbies are diverse. Continue pursuing activities that bring you joy and balance."

# Additional sub-functions for a holistic approach

def analyze_sleep_patterns(sleep_data):
    print(f"Debug - Sleep data: {sleep_data}")
    if sleep_data['consistency'] < 80:
        return "Your sleep pattern shows inconsistencies. Aim for a regular sleep schedule to boost overall mood and perception."
    return "Your sleep patterns are consistent. Keep it up!"

def analyze_diet_nutrition(diet_score):
    print(f"Debug - Diet score: {diet_score}")
    if diet_score < 60:
        return "Your nutrition score is below optimal. Incorporate more whole foods, fruits, and vegetables for better health."
    return "Your diet supports your health. Maintain your balanced meals."

def analyze_physical_activity(activity_level):
    print(f"Debug - Activity level: {activity_level}")
    if activity_level < 3:
        return "Your activity level is low. Increase physical movement through activities you enjoy like walking or cycling."
    return "Your physical activity is sufficient. Keep moving!"

def analyze_hydration_habits(hydration_score):
    print(f"Debug - Hydration score: {hydration_score}")
    if hydration_score < 50:
        return "Hydration is key to maintaining mood and energy. Ensure you drink enough water throughout the day."
    return "Your hydration habits are on point. Stay hydrated!"

def analyze_financial_stress(financial_stress_score):
    print(f"Debug - Financial stress score: {financial_stress_score}")
    if financial_stress_score > 70:
        return "Financial stress can impact overall perception and mental health. Consider financial planning or counseling for support."
    return "Your financial stress is under control. Keep managing your finances wisely."

def analyze_social_connections(social_network_strength):
    print(f"Debug - Social network strength: {social_network_strength}")
    if social_network_strength < 5:
        return "Strengthen your social connections. Regular interactions with close friends and family can improve your perception and happiness."
    return "Your social network is strong. Maintain those relationships."

def analyze_work_life_balance(work_life_score):
    print(f"Debug - Work-life balance score: {work_life_score}")
    if work_life_score < 50:
        return "Your work-life balance could be improved. Allocate time for relaxation and hobbies outside of work."
    return "Your work-life balance is good. Keep nurturing time for personal well-being."

def analyze_self_esteem(self_esteem_score):
    print(f"Debug - Self-esteem score: {self_esteem_score}")
    if self_esteem_score < 40:
        return "Your self-esteem could use a boost. Practice positive affirmations and set achievable goals to build confidence."
    return "Your self-esteem is healthy. Continue with positive self-talk and achieving personal goals."

def analyze_emotional_resilience(resilience_score):
    print(f"Debug - Emotional resilience score: {resilience_score}")
    if resilience_score < 30:
        return "Building emotional resilience can help with challenges. Engage in practices that build coping skills, like mindfulness and reflection."
    return "Your emotional resilience is strong. Maintain these habits to handle stress effectively."

# Main function to analyze perception and compile advice
def compile_perception_analysis(perception_score, **kwargs):
    print(f"Debug - Starting comprehensive perception analysis")
    results = []
    results.append(analyze_perception_score(perception_score, kwargs.get('stress_level'), kwargs.get('mindfulness_practices'), kwargs.get('body_image'), kwargs.get('personality_type'), kwargs.get('sentiment_data'), kwargs.get('instagram_data')))
    results.append(analyze_sleep_patterns(kwargs.get('sleep_data', {})))
    results.append(analyze_diet_nutrition(kwargs.get('diet_score', 70)))
    results.append(analyze_physical_activity(kwargs.get('activity_level', 5)))
    results.append(analyze_hydration_habits(kwargs.get('hydration_score', 60)))
    results.append(analyze_financial_stress(kwargs.get('financial_stress_score', 40)))
    results.append(analyze_social_connections(kwargs.get('social_network_strength', 7)))
    results.append(analyze_work_life_balance(kwargs.get('work_life_score', 70)))

# Expanded perception score analysis incorporating various user data points

def analyze_perception_score(perception_score, stress_level=None, mindfulness_practices=None, body_image=None, personality_type=None, sentiment_data=None, instagram_data=None):
    print(f"Debug - Perception score analysis: perception_score={perception_score}, stress_level={stress_level}, mindfulness_practices={mindfulness_practices}, body_image={body_image}, personality_type={personality_type}, sentiment_data={sentiment_data}, instagram_data={instagram_data}")

    # Provide comprehensive recommendations if the perception score is low
    if perception_score < 5:
        advice = [
            "Your self-reported well-being score is low. Incorporate activities like mindfulness practices, journaling, or guided meditations to improve your mental state.",
            "Engage in physical activities like yoga or moderate exercise, as they can boost mood and reduce stress levels."
        ]
        if stress_level and stress_level > 7:
            advice.append("Your stress levels are high. Prioritize stress reduction techniques such as deep breathing exercises, progressive muscle relaxation, or talking to a mental health professional.")
        if not mindfulness_practices:
            advice.append("Consider starting mindfulness routines, like daily meditation or gratitude journaling, to enhance emotional resilience.")
        if body_image:
            advice.append(analyze_body_image(body_image))
        if personality_type:
            advice.append(analyze_personality_type(personality_type))
        if sentiment_data:
            advice.append(analyze_sentiment_over_time(sentiment_data))
        if instagram_data:
            advice.append(analyze_instagram_hobbies(interests=instagram_data))
        return " ".join(advice)

    # Acknowledge positive perception score and provide encouragement
    else:
        feedback = [
            "Your perception score indicates a good mental state. Keep up with the habits that are contributing to your well-being.",
            "Continuing to engage in self-care routines, balanced work-life practices, and physical activity will help sustain your positive outlook."
        ]
        if mindfulness_practices:
            feedback.append("It’s great that you practice mindfulness regularly. Keep incorporating these practices to maintain emotional balance.")
        return " ".join(feedback)

# Sub-function for analyzing body image from a photo
def analyze_body_image(photo_analysis_result):
    print(f"Debug - Body image analysis result: {photo_analysis_result}")
    if photo_analysis_result['BMI'] > 25:
        return "Your body analysis indicates a higher BMI. Consider a balanced diet and regular exercise to maintain optimal health."
    else:
        return "Your body analysis shows a healthy BMI. Keep maintaining your current lifestyle."

# Sub-function for analyzing personality type
from sklearn.metrics import pairwise_distances

def analyze_personality_type(personality_type):
    print(f"Debug - Personality type: {personality_type}")
    recommendations = {
        'INTJ': "Leverage your strategic thinking by planning regular mental breaks to avoid burnout.",
        'ESFP': "Channel your energy into group activities that promote both social interaction and physical well-being.",
        'INFJ': "Balance your introspective nature with activities that encourage physical activity, such as dance or martial arts.",
        'ENTP': "Keep a varied routine to avoid stagnation and ensure you stay engaged mentally and physically."
    }
    return recommendations.get(personality_type, "Maintain self-reflection and balance your activities to support your well-being.")

# Sub-function for sentiment analysis over time
def analyze_sentiment_over_time(sentiment_data):
    print(f"Debug - Sentiment data analysis: {sentiment_data}")
    avg_sentiment = np.mean(sentiment_data)
    if avg_sentiment < 0:
        return "Your message history indicates overall negative sentiment. Consider reaching out for social support or engaging in positive conversations."
    else:
        return "Your messages reflect positive sentiment. Keep maintaining a positive communication style."

# Sub-function for analyzing Instagram hobbies and interests
def analyze_instagram_hobbies(interests):
    print(f"Debug - Instagram analysis: {interests}")
    if 'outdoor' in interests:
        return "Your interest in outdoor activities suggests a love for nature. Make time for hiking or nature walks to enhance mental well-being."
    elif 'art' in interests:
        return "Artistic hobbies indicate creativity. Consider engaging in painting or crafts to relax and inspire."
    else:
        return "Your hobbies are diverse. Continue pursuing activities that bring you joy and balance."

# Additional sub-functions for a holistic approach

def analyze_sleep_patterns(sleep_data):
    print(f"Debug - Sleep data: {sleep_data}")
    if sleep_data['consistency'] < 80:
        return "Your sleep pattern shows inconsistencies. Aim for a regular sleep schedule to boost overall mood and perception."
    return "Your sleep patterns are consistent. Keep it up!"

def analyze_diet_nutrition(diet_score):
    print(f"Debug - Diet score: {diet_score}")
    if diet_score < 60:
        return "Your nutrition score is below optimal. Incorporate more whole foods, fruits, and vegetables for better health."
    return "Your diet supports your health. Maintain your balanced meals."

def analyze_physical_activity(activity_level):
    print(f"Debug - Activity level: {activity_level}")
    if activity_level < 3:
        return "Your activity level is low. Increase physical movement through activities you enjoy like walking or cycling."
    return "Your physical activity is sufficient. Keep moving!"

def analyze_hydration_habits(hydration_score):
    print(f"Debug - Hydration score: {hydration_score}")
    if hydration_score < 50:
        return "Hydration is key to maintaining mood and energy. Ensure you drink enough water throughout the day."
    return "Your hydration habits are on point. Stay hydrated!"

def analyze_financial_stress(financial_stress_score):
    print(f"Debug - Financial stress score: {financial_stress_score}")
    if financial_stress_score > 70:
        return "Financial stress can impact overall perception and mental health. Consider financial planning or counseling for support."
    return "Your financial stress is under control. Keep managing your finances wisely."

def analyze_social_connections(social_network_strength):
    print(f"Debug - Social network strength: {social_network_strength}")
    if social_network_strength < 5:
        return "Strengthen your social connections. Regular interactions with close friends and family can improve your perception and happiness."
    return "Your social network is strong. Maintain those relationships."

def analyze_work_life_balance(work_life_score):
    print(f"Debug - Work-life balance score: {work_life_score}")
    if work_life_score < 50:
        return "Your work-life balance could be improved. Allocate time for relaxation and hobbies outside of work."
    return "Your work-life balance is good. Keep nurturing time for personal well-being."

def analyze_self_esteem(self_esteem_score):
    print(f"Debug - Self-esteem score: {self_esteem_score}")
    if self_esteem_score < 40:
        return "Your self-esteem could use a boost. Practice positive affirmations and set achievable goals to build confidence."
    return "Your self-esteem is healthy. Continue with positive self-talk and achieving personal goals."

def analyze_emotional_resilience(resilience_score):
    print(f"Debug - Emotional resilience score: {resilience_score}")
    if resilience_score < 30:
        return "Building emotional resilience can help with challenges. Engage in practices that build coping skills, like mindfulness and reflection."
    return "Your emotional resilience is strong. Maintain these habits to handle stress effectively."

# Main function to analyze perception and compile advice
def compile_perception_analysis(perception_score, **kwargs):
    print(f"Debug - Starting comprehensive perception analysis")
    results = []
    results.append(analyze_perception_score(perception_score, kwargs.get('stress_level'), kwargs.get('mindfulness_practices'), kwargs.get('body_image'), kwargs.get('personality_type'), kwargs.get('sentiment_data'), kwargs.get('instagram_data')))
    results.append(analyze_sleep_patterns(kwargs.get('sleep_data', {})))
    results.append(analyze_diet_nutrition(kwargs.get('diet_score', 70)))
    results.append(analyze_physical_activity(kwargs.get('activity_level', 5)))
    results.append(analyze_hydration_habits(kwargs.get('hydration_score', 60)))
    results.append(analyze_financial_stress(kwargs.get('financial_stress_score', 40)))
    results.append(analyze_social_connections(kwargs.get('social_network_strength', 7)))
    results.append(analyze_work_life_balance(kwargs.get('work_life_score', 70)))

