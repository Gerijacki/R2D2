import discord
from discord.ext import commands
import random

# Define the Fun cog
class Fun(commands.Cog):
    """A cog for fun commands and games."""

    def __init__(self, bot):
        """Initialize the cog with a reference to the bot."""
        self.bot = bot

    @commands.command(name="roll")
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format (e.g., 2d6)."""
        try:
            rolls, limit = map(int, dice.split("d"))
            result = ", ".join(str(random.randint(1, limit)) for _ in range(rolls))
            await ctx.send(f"{ctx.author.mention} rolled: {result}")
        except ValueError:
            await ctx.send("Format must be in NdN (e.g., 2d6).")

# Required setup function to add the cog to the bot
async def setup(bot):
    """Adds this cog to the bot."""
    await bot.add_cog(Fun(bot))
