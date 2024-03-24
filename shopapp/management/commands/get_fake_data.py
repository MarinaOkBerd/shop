import math
import random

from django.core.management.base import BaseCommand

from shopapp.models import Customer, Product, Order


class Command(BaseCommand):
    help = "Get fake data"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        qty_custs = count
        qty_prods = count ** 3
        qty_orders = count * 2

        customers = []
        products = []

        for i in range(1, qty_custs + 1):
            customer = Customer(name=f'name_{i}', email=f'email{i}@em.em',
                                phone=f'89{random.randint(100_000_000, 999_999_999)}',
                                address=f'г {i},{i}, {i}, {i}')
            customer.save()
            customers.append(customer)

        for i in range(1, qty_prods + 1):
            product = Product(title=f'title_{i}', description=f'description_{i}',
                              price=random.randint(100, 100_000)/math.pi,
                              amount=random.randint(1, 200),
                              )

            product.save()
            products.append(product)

        for i in range(1, qty_orders + 1):
            order = Order(customer=random.choice(customers),
                          total_price=0)
            order.save()
            sum = 0
            for _ in range(random.randint(1, qty_custs)):
                product = random.choice(products)
                sum += product.price
                order.products.add(product)
                order.save()
            order.total_price = sum
            order.save()