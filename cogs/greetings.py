import discord
from discord.ext import commands

# Define the Greetings cog
class Greetings(commands.Cog):
    """A cog for simple greeting commands."""

    def __init__(self, bot):
        """Initialize the cog with a reference to the bot."""
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx):
        """Responds with a friendly greeting."""
        # Sends a hello message mentioning the user who invoked the command
        await ctx.send(f"Hello {ctx.author.mention}!")

# Required setup function to add the cog to the bot
async def setup(bot):
    """Adds this cog to the bot."""
    await bot.add_cog(Greetings(bot))
