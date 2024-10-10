import requests
import json


url_events = "https://api.bettingpros.com/v3/events?sport=NFL&week=6&season=2024"
response_events = requests.get(url_events, headers=headers)
if response_events.status_code == 200:
    events_data = response_events.json()
    print(json.dumps(events_data, indent=4))
else:
    print(f"Failed to fetch events: {response_events.status_code}")

