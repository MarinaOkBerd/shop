import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


from .models import Product, Order, Customer

from .forms import ProductFormWidget

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'{request} request received')
    return render(request, 'index.html')


def shopapp(request):
    logger.info(f'{request} request received')
    return render(request, 'shopapp/shopapp.html')


def customers(request):
    logger.info(f'{request} request received')
    customers = Customer.objects.all()
    context = {'title': 'Customers',
               'name': 'customer_orders',
               'items': customers}
    return render(request, 'shopapp/items.html', context)


def products(request):
    logger.info(f'{request} request received')
    products = Product.objects.all()
    context = {'title': 'Products',
               'name': 'product_id',
               'items': products}
    return render(request, 'shopapp/items.html', context)


def orders(request):
    logger.info(f'{request} request received')
    orders = Order.objects.all()
    context = {'title': 'Orders',
               'name': 'order_products',
               'items': orders}
    return render(request, 'shopapp/items.html', context)


def order_products(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products = Product.objects.filter(order=order).all()
    context = {'title': order.id,
               'list': 'Order',
               'items': products,
               'name': 'product_id'}
    return render(request, 'shopapp/item_id.html', context)


def customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).all()
    context = {'title': customer.id,
               'list': 'Customer',
               'items': orders,
               'name': 'order_products'}
    return render(request, 'shopapp/item_id.html', context)


def product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'title': product.id,
               'list': 'Product',
               'product': product}
    return render(request, 'shopapp/product_id.html', context)


def customer_products(request, customer_id, period=7):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer,
                                  date_ordered__gt=(timezone.now() - timezone.timedelta(days=period))).all()
    products = [product for order in orders for product in order.products.all()]
    context = {'title': customer.id,
               'list': 'Customer',
               'items': products,
               'name': 'order_products'}
    return render(request, 'shopapp/item_id.html', context)


def add_product_form(request):
    if request.method == 'POST':
        form = ProductFormWidget(request.POST, request.FILES)
        message = 'Некорректные данные'
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            date_added = form.cleaned_data['date_added']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f'Получили {title=}, {description=}, {price=}, {amount=},'
                        f'{date_added=}', f'фото загружено')
            product = Product(title=title, description=description, price=price,
                              amount=amount, date_added=date_added, image=image)
            product.save()
            message = 'Товар добавлен'
    else:
        form = ProductFormWidget()
        message = 'Заполните данные для добавления товара'
    context = {'title': 'Форма товара',
               'form': form,
               'message': message,
               'name': 'add_product_form'}
    return render(request, 'shopapp/product_form.html', context)
from django.shortcuts import render

