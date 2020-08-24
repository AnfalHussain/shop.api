from django.contrib import admin
from .models import Product, Order, Basket, Address


admin.site.site_header = 'Shop Dashboard'


class ProductAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'stock',
                    'active')
    search_fields = ('name',)
    list_filter = ('active',)
    ordering = ['name']
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(active=True)
        if rows_updated == 1:
            message_bit = "1 product was"
        else:
            message_bit = "%s products were" % rows_updated
        self.message_user(request, "%s successfully activated." % message_bit)
    make_active.short_description = "Activate products"

    def make_inactive(self, request, queryset):
        rows_updated = queryset.update(active=False)
        if rows_updated == 1:
            message_bit = "1 product was"
        else:
            message_bit = "%s products were" % rows_updated
        self.message_user(request, "%s successfully deactived." % message_bit)
    make_inactive.short_description = "Deactivate products"


class OrderAdmin (admin.ModelAdmin):

    list_display = ('order_ref', 'date_time', 'total')
    search_fields = ('order_ref',)
    list_filter = ('date_time',)
    date_hierarchy = 'date_time'


admin.site.register(Product, ProductAdmin)
admin.site.register(Address)
admin.site.register(Order, OrderAdmin)
admin.site.register(Basket)
