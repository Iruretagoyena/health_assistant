import random
import json
from datetime import datetime, timedelta

def generate_sleep_profile(filename):
    """
    Generate a realistic sleep profile with 30 days of data and save it to a JSON file.
    
    Args:
        filename (str): The name of the JSON file to save the sleep profile data.
    """
    
    # Basic user information
    user_profile = {
        "user_id": "test_user_123",
        "age": 32,
        "gender": "female",
        "weight_kg": 65,
        "height_cm": 168,
        "activity_level": "moderate",  # sedentary, moderate, active
        "self_reported_issues": ["difficulty falling asleep", "occasional mid-night wakings"],
        
        # Goals and preferences
        "sleep_goals": {
            "target_sleep_duration": "8 hours",
            "target_bedtime": "22:30",
            "target_wake_time": "06:30"
        }
    }

    # Last 30 days of sleep metrics
    sleep_data = {
        "daily_metrics": [],
        "aggregated_metrics": {}
    }

    # Generate daily sleep data
    base_date = datetime.now() - timedelta(days=30)
    
    # Simulate realistic patterns
    for day in range(30):
        current_date = base_date + timedelta(days=day)
        
        # Simulate some realistic variations
        if day % 7 in [5, 6]:  # Weekend pattern
            sleep_duration = round(random.uniform(7.5, 8.5), 2)
            sleep_efficiency = round(random.uniform(88, 94), 1)
        else:  # Weekday pattern
            sleep_duration = round(random.uniform(6.2, 7.8), 2)
            sleep_efficiency = round(random.uniform(82, 90), 1)

        daily_data = {
            "date": current_date.strftime("%Y-%m-%d"),
            
            # Sleep duration metrics
            "total_sleep_duration": sleep_duration,
            "time_in_bed": round(sleep_duration / (sleep_efficiency/100), 2),
            "sleep_efficiency": sleep_efficiency,
            
            # Sleep stages (in minutes)
            "sleep_stages": {
                "deep_sleep": round(sleep_duration * random.uniform(0.15, 0.25) * 60),
                "light_sleep": round(sleep_duration * random.uniform(0.45, 0.55) * 60),
                "rem_sleep": round(sleep_duration * random.uniform(0.20, 0.25) * 60),
                "awake": round(sleep_duration * random.uniform(0.05, 0.15) * 60)
            },
            
            # Sleep timing
            "sleep_schedule": {
                "bedtime": (current_date - timedelta(hours=random.uniform(8, 10))).strftime("%H:%M"),
                "wake_time": (current_date + timedelta(hours=sleep_duration)).strftime("%H:%M"),
                "time_to_fall_asleep": round(random.uniform(15, 45)),
                "number_of_awakenings": round(random.uniform(1, 4))
            },
            
            # Environmental factors
            "environment": {
                "temperature_celsius": round(random.uniform(18, 22), 1),
                "noise_level_db": round(random.uniform(25, 35)),
                "light_level_lux": round(random.uniform(0, 5))
            },
            
            # Physiological metrics
            "physiological": {
                "average_hr_sleep": round(random.uniform(55, 65)),
                "min_hr_sleep": round(random.uniform(48, 54)),
                "average_hrv_ms": round(random.uniform(35, 55)),
                "respiratory_rate": round(random.uniform(14, 16), 1),
                "body_temperature_celsius": round(random.uniform(36.3, 36.7), 1)
            }
        }
        
        sleep_data["daily_metrics"].append(daily_data)

    # Calculate aggregated metrics
    sleep_data["aggregated_metrics"] = {
        "average_metrics": {
            "avg_sleep_duration": round(sum(d["total_sleep_duration"] for d in sleep_data["daily_metrics"]) / 30, 2),
            "avg_sleep_efficiency": round(sum(d["sleep_efficiency"] for d in sleep_data["daily_metrics"]) / 30, 1),
            "avg_deep_sleep_percentage": round(sum(d["sleep_stages"]["deep_sleep"] for d in sleep_data["daily_metrics"]) / 
                                            sum(d["total_sleep_duration"] * 60 for d in sleep_data["daily_metrics"]) * 100, 1),
            "avg_rem_percentage": round(sum(d["sleep_stages"]["rem_sleep"] for d in sleep_data["daily_metrics"]) /
                                     sum(d["total_sleep_duration"] * 60 for d in sleep_data["daily_metrics"]) * 100, 1)
        },
        
        "sleep_patterns": {
            "weekday_avg_duration": round(sum(d["total_sleep_duration"] for d in sleep_data["daily_metrics"] 
                                            if datetime.strptime(d["date"], "%Y-%m-%d").weekday() < 5) / 22, 2),
            "weekend_avg_duration": round(sum(d["total_sleep_duration"] for d in sleep_data["daily_metrics"]
                                            if datetime.strptime(d["date"], "%Y-%m-%d").weekday() >= 5) / 8, 2),
            "social_jet_lag": round(abs(random.uniform(0.5, 1.5)), 1)  # hours difference between weekday/weekend sleep midpoint
        },
        
        "sleep_quality_indicators": {
            "consistent_sleep_schedule": False,
            "optimal_deep_sleep": True,
            "efficient_sleep": True,
            "sleep_debt": round(random.uniform(3, 5), 1)  # hours
        },
        
        "trends": {
            "sleep_duration_trend": "decreasing",  # increasing, decreasing, stable
            "sleep_efficiency_trend": "stable",
            "deep_sleep_trend": "stable",
            "notable_changes": [
                "Decreased average sleep duration by 30 minutes over past week",
                "Improved sleep efficiency on weekends",
                "Consistent deep sleep percentage"
            ]
        }
    }

    # Construct the complete profile
    profile_data = {
        "user_profile": user_profile,
        "sleep_data": sleep_data
    }

    # Write the profile data to the specified JSON file
    with open(filename, "w") as f:
        json.dump(profile_data, f, indent=2)

    print(f"Sleep profile data has been written to '{filename}'")

# Example usage
generate_sleep_profile("generated_sleep_data.json")
