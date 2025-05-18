from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'created', 'updated')
    list_filter = ('is_available', 'created', 'updated')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'
    ordering = ('-created',)

admin.site.register(Product, ProductAdmin)