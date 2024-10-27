import discord
from discord.ext import commands
import config
import os

# Set up the bot's intents, which specify what types of events it will listen to
# message_content=True is needed for reading message content
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot instance with a command prefix and specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: on_ready is triggered once the bot successfully connects to Discord
@bot.event
async def on_ready():
    """Triggered when the bot has connected to Discord and is ready."""
    print(f"Logged in as {bot.user}")  # Print bot login confirmation
    # Dynamically load all cogs (extensions) in the cogs folder
    for filename in os.listdir('./cogs'):
        # Only load Python files, ignoring __init__.py and others
        if filename.endswith('.py') and filename != '__init__.py':
            # Remove the .py extension and load the cog
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"Loaded {filename[:-3]} module.")  # Confirm each loaded module

# Start the bot using the token from config.py
bot.run(config.DISCORD_TOKEN)
