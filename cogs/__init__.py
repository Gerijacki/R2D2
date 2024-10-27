import os
import importlib

# Automatically import all modules in this directory
for filename in os.listdir(os.path.dirname(__file__)):
    if filename.endswith('.py') and filename != '__init__.py':
        # Dynamically import each module in the cogs folder
        module_name = filename[:-3]
        importlib.import_module(f'.{module_name}', package=__name__)
