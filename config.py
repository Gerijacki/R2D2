# config.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Assign loaded environment variables to constants
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  # Discord bot token
GUILD_ID = int(os.getenv("GUILD_ID"))       # Discord guild (server) ID
