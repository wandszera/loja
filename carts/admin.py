from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
    search_fields = ('cart_id',)
    list_filter = ('date_added',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
    list_filter = ('product', 'cart', 'is_active')
    search_fields = ('product__name', 'cart__cart_id')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
