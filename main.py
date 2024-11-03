import os
import pandas as pd
import json


# Sample script for creating a user database
with open("project/database/create_user_db.py", "w") as db_file:
    db_file.write("""
import json

user_data = {
    "user_id": "001",
    "name": "John Doe",
    "age": 30,
    "health_data_sources": ["Apple Health", "EightSleep", "Oura Ring"],
    "interview_notes": "User has concerns about sleep and energy levels."
}

# Save user data to a database file
with open('../database/user_001.json', 'w') as user_file:
    json.dump(user_data, user_file)

print("User database created.")
"""
)
