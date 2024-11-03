
import json

# Load processed data
with open('../output/processed_data.json', 'r') as infile:
    data = json.load(infile)

recommendations = []

for user, records in data.items():
    for record in records:
        sleep_hours = record.get('sleep_hours', 0)
        steps = record.get('steps', 0)

        # Simple rule-based recommendations
        if sleep_hours < 5:
            recommendations.append(f"[User: {user}] We need to pay attention to our sleep. Sleep is the #1 most important habit for your health and well-being.")
        if steps >= 10000:
            recommendations.append(f"[User: {user}] Congratulations for nailing 10k steps a day this week!")

# Print recommendations and save to a file
with open('../output/recommendations.txt', 'w') as rec_outfile:
    for rec in recommendations:
        print(rec)
        rec_outfile.write(rec + '')

print("Recommendations generated.")
