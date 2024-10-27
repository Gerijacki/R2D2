import discord
from discord.ext import commands

# Define the Moderation cog
class Moderation(commands.Cog):
    """A cog for basic moderation commands."""

    def __init__(self, bot):
        """Initialize the cog with a reference to the bot."""
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)  # Restrict to users with kick permissions
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a specified member from the server."""
        # Attempts to kick the specified member
        try:
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention} was kicked for: {reason}")
        except discord.Forbidden:
            # If the bot lacks permissions, inform the user
            await ctx.send("I do not have permission to kick this user.")
        except Exception as e:
            # Log any other unexpected errors
            await ctx.send(f"An error occurred: {e}")

# Required setup function to add the cog to the bot
async def setup(bot):
    """Adds this cog to the bot."""
    await bot.add_cog(Moderation(bot))
