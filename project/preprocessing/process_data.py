import pandas as pd
import os
import json
import requests

def preprocess_health_data(file_path):
    try:
        data = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_json(file_path)
        # Basic preprocessing steps: handling missing values, normalizing units, etc.
        data.fillna(method='ffill', inplace=True)
        print(f"Data from {file_path} processed successfully.")
        return data
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return pd.DataFrame()

# Preprocess all data files in the data directory
data_dir = '../data/'
processed_data = {}
for filename in os.listdir(data_dir):
    if filename.endswith('.csv') or filename.endswith('.json'):
        filepath = os.path.join(data_dir, filename)
        processed_data[filename] = preprocess_health_data(filepath)

# Save processed data for further analysis
with open('../output/processed_data.json', 'w') as outfile:
    json.dump({k: v.to_dict(orient='records') for k, v in processed_data.items()}, outfile)

print("Preprocessing completed.")

def fetch_apple_health_data(token):
    # Placeholder for fetching Apple Health data via API
    response = requests.get('https://api.apple.com/health/data', headers={'Authorization': f'Bearer {token}'})
    return response.json() if response.status_code == 200 else {}

def fetch_oura_data(token):
    response = requests.get('https://api.ouraring.com/v1/userinfo', headers={'Authorization': f'Bearer {token}'})
    return response.json() if response.status_code == 200 else {}

def fetch_eightsleep_data(token):
    response = requests.get('https://api.eightsleep.com/v1/sleep', headers={'Authorization': f'Bearer {token}'})
    return response.json() if response.status_code == 200 else {}

def fetch_strava_data(token):
    response = requests.get('https://www.strava.com/api/v3/athlete', headers={'Authorization': f'Bearer {token}'})
    return response.json() if response.status_code == 200 else {}

def preprocess_health_data(data_sources):
    all_data = []
    for source, data in data_sources.items():
        df = pd.DataFrame(data)
        df['source'] = source  # Tag data with its source
        all_data.append(df)
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.fillna(method='ffill', inplace=True)
    return combined_df

# Example of how to use the fetch functions
apple_health_token = 'YOUR_APPLE_HEALTH_TOKEN'
oura_token = 'YOUR_OURA_TOKEN'
eightsleep_token = 'YOUR_EIGHTSLEEP_TOKEN'
strava_token = 'YOUR_STRAVA_TOKEN'

# Fetch data from various sources
data_sources = {
    'Apple Health': fetch_apple_health_data(apple_health_token),
    'Oura': fetch_oura_data(oura_token),
    'EightSleep': fetch_eightsleep_data(eightsleep_token),
    'Strava': fetch_strava_data(strava_token)
}

# Preprocess and save data
combined_data = preprocess_health_data(data_sources)
combined_data.to_csv('../output/combined_data.csv', index=False)
print("Data from multiple sources combined and saved successfully.")