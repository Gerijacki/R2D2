# bot.py
import discord
from discord.ext import commands
import os
from config import TOKEN, PREFIX

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

# Cargar Cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)
