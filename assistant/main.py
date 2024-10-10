# main.py

import json
import os
from datetime import datetime
from settings.api_config import API_BASE_URL, API_HEADERS, ENDPOINTS
from functions.api_call import make_api_call
from functions.format_games import format_games
from settings.paths_config import GAME_INFO_DIR
import requests  # Add this if not already imported

def handle_response(response):
    try:
        response.raise_for_status()
        data = response.json()
        format_games(data)
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
    except json.JSONDecodeError:
        print("Failed to parse JSON response.")
        return None

def fetch_games():
    current_year = datetime.now().year
    week = input("Enter the week number: ").strip()

    # Build the full URL using the endpoint and user input
    endpoint = ENDPOINTS['game_info'].format(week=week, season=current_year)
    url = f"{API_BASE_URL}{endpoint}"

    # Make the API call and specify the call type for saving
    response = make_api_call(url, API_HEADERS, call_type="game_info")

    # Handle the response and format it for display
    handle_response(response)

def main():
    print("Welcome to the Sports Data Assistant!")
    print("Type 'help' to see available commands.")

    while True:
        command = input("\nEnter a command: ").strip().lower()

        if command in ["exit", "quit"]:
            print("Exiting the application. Goodbye!")
            break
        elif command == "help":
            print("\nAvailable commands:")
            print("- games: Fetch and display game information")
            print("- exit or quit: Exit the application")
        elif command == "games":
            fetch_games()
        else:
            print(f"Unknown command: '{command}'. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()

