import json

user_data = {
    "user_id": "001",
    "name": "John Doe",
    "age": 30,
    "health_data_sources": ["Apple Health", "EightSleep", "Oura Ring"],
    "interview_notes": "User has concerns about sleep and energy levels."
}

# Save user data to a database file
with open('../database/user_001.json', 'a+') as user_file:
    json.dump(user_data, user_file)

print("User database created.")
