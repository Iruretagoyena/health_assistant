import requests
import csv
import json

def fetch_oura_data(start_date, end_date, token):
    url = 'https://api.ouraring.com/v2/usercollection/daily_activity'
    params = {
        'start_date': start_date,
        'end_date': end_date
    }
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()  # Return the parsed JSON data if successful
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def save_data_to_csv(data, filename='oura_data.csv'):
    # Open the file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write headers
        if data and 'data' in data:
            headers = data['data'][0].keys()  # Extract keys from the first data item as headers
            writer.writerow(headers)

            # Write data rows
            for entry in data['data']:
                writer.writerow(entry.values())
        else:
            print("No data available to save.")

# Usage
token = 'DYFVHF73YGUXZWYMVMK6TCPFQTO4R6BX'
start_date = '2023-11-01'
end_date = '2024-12-01'

# Fetch data
oura_data = fetch_oura_data(start_date, end_date, token)

# Save data to CSV
if oura_data:
    save_data_to_csv(oura_data, 'oura_data.csv')
    print("Data saved to oura_data.csv")
else:
    print("No data to save.")
