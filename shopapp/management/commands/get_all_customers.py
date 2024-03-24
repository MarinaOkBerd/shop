from django.core.management.base import BaseCommand

from shopapp.models import Customer


class Command(BaseCommand):
    help = "Get all customers"

    def handle(self, *args, **kwargs):
        customer = Customer.objects.all()
        self.stdout.write(f'{customer}')