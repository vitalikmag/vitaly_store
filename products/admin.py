from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'stripe_product_price_id', 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name', 'price', 'quantity')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity',)
    readonly_fields = ('created_timestamp',)
    extra = 1
