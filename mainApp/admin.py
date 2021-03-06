from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Vegetables)
admin.site.register(Fruits)
admin.site.register(KitchenCategory)
admin.site.register(FrozenFoods)
admin.site.register(Pulses)
admin.site.register(Bakery)
admin.site.register(Beverages)
admin.site.register(Snacks)
admin.site.register(Spices)
admin.site.register(Cart)
admin.site.register(WishList)
admin.site.register(Contact)
admin.site.register(CheckOut)
# admin.site.register(OrdersPlaced)

class Order(admin.ModelAdmin):
    readonly_fields=['date']


admin.site.register(OrdersPlaced, Order)