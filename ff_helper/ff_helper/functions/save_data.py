# functions/save_data.py

import json
import csv

def save_data_to_file(data, file_path, file_format):
    try:
        if file_format == 'json':
            # Save as JSON
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data saved as JSON to {file_path}")
        
        elif file_format == 'csv':
            # Save as CSV
            if isinstance(data, dict) and 'events' in data:
                keys = data['events'][0].keys()  # Extract keys from the first event
                with open(file_path, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(data['events'])  # Write the events as rows
                print(f"Data saved as CSV to {file_path}")
            else:
                print("Data format is not supported for CSV export.")

        else:
            print(f"Unsupported file format: {file_format}")
    
    except Exception as e:
        print(f"Failed to save data: {e}")

