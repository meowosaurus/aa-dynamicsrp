from django.core.management.base import BaseCommand
from dynamicsrp.data_utils import add_settings, add_ships

class Command(BaseCommand):
    help = 'Populate database with predefined data'

    def handle(self, *args, **kwargs):
        add_settings()
        self.stdout.write(self.style.SUCCESS('Settings successfully populated!'))
        add_ships()
        self.stdout.write(self.style.SUCCESS('Ship data successfully populated!'))
