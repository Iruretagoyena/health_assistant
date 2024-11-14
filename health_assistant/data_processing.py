from health_assistant.generate_sleep_profile import generate_sleep_profile
import json

def process_user_data(user_data):
    # Simulate data analysis (e.g., averages, summaries)
    return {
        "average_sleep_quality": sum(user_data['sleep_quality']) / len(user_data['sleep_quality']),
        "activity_summary": f"User's average step count: {sum(user_data['steps']) / len(user_data['steps'])}",
        "heart_rate_analysis": f"Average heart rate is {sum(user_data['heart_rate']) / len(user_data['heart_rate'])} bpm"
    }

def get_generated_sleep_data() -> str :
    file_name = "generated_sleep_data.json"
    generate_sleep_profile(file_name)
    return load_and_format_sleep_data(file_name)

def load_and_format_sleep_data(filename):
    """
    Load sleep data from a JSON file and format it as a readable string.
    
    Args:
        filename (str): The path to the JSON file.
        
    Returns:
        str: Formatted string containing the sleep data.
    """
    # Load data from the JSON file
    with open(filename, "r") as f:
        data = json.load(f)

    # Format the user profile section
    user_profile = data["user_profile"]
    profile_str = (
        f"User Profile:\n"
        f"User ID: {user_profile['user_id']}\n"
        f"Age: {user_profile['age']}\n"
        f"Gender: {user_profile['gender']}\n"
        f"Weight: {user_profile['weight_kg']} kg\n"
        f"Height: {user_profile['height_cm']} cm\n"
        f"Activity Level: {user_profile['activity_level']}\n"
        f"Self-Reported Issues: {', '.join(user_profile['self_reported_issues'])}\n"
        f"Sleep Goals: {user_profile['sleep_goals']['target_sleep_duration']} of sleep, "
        f"bedtime at {user_profile['sleep_goals']['target_bedtime']}, "
        f"wake time at {user_profile['sleep_goals']['target_wake_time']}\n"
    )

    # Format the aggregated metrics section
    aggregated_metrics = data["sleep_data"]["aggregated_metrics"]
    avg_metrics = aggregated_metrics["average_metrics"]
    sleep_patterns = aggregated_metrics["sleep_patterns"]
    trends = aggregated_metrics["trends"]

    metrics_str = (
        f"\nAggregated Sleep Metrics:\n"
        f"Average Sleep Duration: {avg_metrics['avg_sleep_duration']} hours\n"
        f"Average Sleep Efficiency: {avg_metrics['avg_sleep_efficiency']}%\n"
        f"Deep Sleep Percentage: {avg_metrics['avg_deep_sleep_percentage']}%\n"
        f"REM Sleep Percentage: {avg_metrics['avg_rem_percentage']}%\n"
        f"Weekday Avg Duration: {sleep_patterns['weekday_avg_duration']} hours\n"
        f"Weekend Avg Duration: {sleep_patterns['weekend_avg_duration']} hours\n"
        f"Social Jet Lag: {sleep_patterns['social_jet_lag']} hours\n"
        f"Trends:\n"
        f"- Sleep Duration Trend: {trends['sleep_duration_trend']}\n"
        f"- Sleep Efficiency Trend: {trends['sleep_efficiency_trend']}\n"
        f"- Deep Sleep Trend: {trends['deep_sleep_trend']}\n"
        f"- Notable Changes: {', '.join(trends['notable_changes'])}\n"
    )

    # Combine all sections into a single prompt string
    prompt = f"{profile_str}\n{metrics_str}"
    return prompt
