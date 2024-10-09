import json
import os
from datetime import datetime
from settings.api_config import API_BASE_URL, API_HEADERS, ENDPOINTS
from functions.api_call import make_api_call
from functions.format_games import format_games  # Import the format_games function
from settings.paths_config import GAME_INFO_DIR

def handle_response(response):
    try:
        response.raise_for_status()
        data = response.json()
        format_games(data)  # Format and display the game info in the terminal
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
    except json.JSONDecodeError:
        print("Failed to parse JSON response.")
        return None

def main():
    # Automatically get the current year
    current_year = datetime.now().year

    # Ask for the week number
    week = input("Enter the week number: ").strip()

    # Build the full URL using the endpoint and user input
    user_input = "game_info"  # Fixed for now
    endpoint = ENDPOINTS[user_input].format(week=week, season=current_year)
    url = f"{API_BASE_URL}{endpoint}"

    # Make the API call and specify the call type for saving
    response = make_api_call(url, API_HEADERS, call_type="game_info")

    # Handle the response and format it for display
    handle_response(response)

if __name__ == "__main__":
    main()

