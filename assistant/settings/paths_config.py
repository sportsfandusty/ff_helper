# settings/paths_config.py

import os

# Base directory for data storage
BASE_DATA_DIR = os.path.join(os.getcwd(), "data")

# Subdirectories
RAW_DIR = os.path.join(BASE_DATA_DIR, "raw")
GAME_INFO_DIR = os.path.join(RAW_DIR, "game_info")

# Ensure these directories exist
os.makedirs(GAME_INFO_DIR, exist_ok=True)

