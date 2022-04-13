"""
cart/apps.py: app config file for cart app.
"""

# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    Cart app Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
