# functions/api_call.py

import requests
import json
import os
from datetime import datetime
from settings.paths_config import RAW_DIR  # Import the directory for saving raw data

def make_api_call(url, headers, call_type):
    response = requests.get(url, headers=headers)
    
    # Save raw data with a timestamp
    if response.status_code == 200:
        save_raw_data(response.json(), call_type)
    
    return response

def save_raw_data(data, call_type):
    # Generate a filename with a timestamp and API call description
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"raw_{call_type}_{timestamp}.json"
    file_path = os.path.join(RAW_DIR, file_name)

    # Save the raw data as JSON
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Raw data saved to {file_path}")
    except Exception as e:
        print(f"Failed to save raw data: {e}")

