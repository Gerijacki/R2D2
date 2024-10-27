# cogs/fun.py
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Lanza un dado"""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Formato incorrecto. Usa: !roll XdY')
            return

        result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
        await ctx.send(f'Roll: {result}')

def setup(bot):
    bot.add_cog(Fun(bot))
