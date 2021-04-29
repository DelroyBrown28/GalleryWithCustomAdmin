from django.contrib import admin
from .models import (Product,
                     OrderItem,
                     Order,
                     SizeVariation,
                     Address,
                     Payment)


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    readonly_fields = ['updated', 'created']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Product


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_1',
        'address_2',
        'postcode',
        'town_or_city',
        'address_type',
    ]


class SizeVariationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'size_price',
    ]


admin.site.register(Address, AddressAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SizeVariation, SizeVariationAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Payment)
