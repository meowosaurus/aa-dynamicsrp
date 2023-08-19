from django.core.management.base import BaseCommand
from dynamicsrp.data_utils import add_settings, add_ships
from dynamicsrp import __title__, __version__

class Command(BaseCommand):
    help = 'Populate database with predefined data'

    prefix = "[" + __title__ + " " + __version__ + "] "

    def handle(self, *args, **kwargs):

        self.stdout.write(self.prefix + 'Loading data might take a while.')
        add_settings()
        self.stdout.write(self.style.SUCCESS(self.prefix + 'Settings successfully populated!'))
        add_ships()
        self.stdout.write(self.style.SUCCESS(self.prefix + 'Ship data successfully populated!'))
