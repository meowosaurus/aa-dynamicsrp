"""App Configuration"""

# Django
from django.apps import AppConfig

# AA dynamicsrp App
from dynamicsrp import __version__


class dynamicsrpConfig(AppConfig):
    """App Config"""

    name = "dynamicsrp"
    label = "dynamicsrp"
    verbose_name = f"dynamicsrp App v{__version__}"
