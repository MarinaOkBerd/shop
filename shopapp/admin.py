from django.contrib import admin
from .models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    ordering = ['name']
    list_filer = ['-date_registered']
    search_fields = ['name', 'email', 'phone', 'address']
    search_help_text = 'Поиск клиента по имени, email, телефону, адресу'
    readonly_fields = ['date_registered']
    fields = ['name', 'email', 'phone', 'address', 'date_registered']
    list_per_page = 10


@admin.action(description="Обнулить количество товара")
def reset_amount(modeladmin, request, queryset):
    queryset.update(amount=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'amount', 'image']
    ordering = ['title', '-date_added']
    list_filter = ['price', 'amount', 'date_added']
    search_fields = ['title', 'description']
    search_help_text = 'Поиск товаров'
    actions = [reset_amount]
    list_per_page = 20
    fieldsets = [
        (
            'Информация',
            {
                'classes': ['wide'],
                'fields': ['title', 'description', 'image'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'classes': ['collapse'],
                'fields': ['price', 'amount'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_ordered', 'customer', 'total_price']
    ordering = ['id', '-date_ordered']
    list_filter = ['customer', 'products']
    readonly_fields = ['total_price', 'date_ordered']
    fields = ['customer', 'products', 'total_price', 'date_ordered']
    list_per_page = 10


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
