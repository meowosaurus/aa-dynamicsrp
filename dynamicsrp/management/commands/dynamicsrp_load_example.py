from django.core.management.base import BaseCommand
from dynamicsrp.data_utils import add_example_reimbursements, add_example_payouts

class Command(BaseCommand):
    help = 'Populate database with example data'

    def handle(self, *args, **kwargs):
        add_example_reimbursements()
        self.stdout.write(self.style.SUCCESS('Example reimbursement columns successfully populated!'))
        add_example_payouts()
