#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Importing the required modules
import os  # Provides functions to interact with the operating system
import sys # Provides access to system-specific parameters and functions


def main():
    """Run administrative tasks."""
    # Sets the default settings module for the Django project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rabbani_Site.settings')
    try:
        # Imports Django's function to execute command-line commands
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raises an error if Django is not installed or if the environment is not set up correctly
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        # Executes the command-line arguments passed to the scrip
    execute_from_command_line(sys.argv)

# Ensures the script runs only when executed directly, not when imported
if __name__ == '__main__':
    main()
