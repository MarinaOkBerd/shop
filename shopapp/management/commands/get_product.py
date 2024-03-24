from django.core.management.base import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    help = "Get product"

    def handle(self, *args, **kwargs):
        product = Product(title='Product', description='', price=99.99, amount=25)
        product.save()
        self.stdout.write(f'{product}')