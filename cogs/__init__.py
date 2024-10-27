# cogs/__init__.py

def setup(bot):
    """Carga todos los cogs en el bot."""
    # Aquí podrías cargar los cogs automáticamente si no quieres hacerlo en bot.py
    from .admin import Admin
    from .fun import Fun
    from .utility import Utility

    bot.add_cog(Admin(bot))
    bot.add_cog(Fun(bot))
    bot.add_cog(Utility(bot))
