from django.contrib import admin
from .models import Product, Variation

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'created', 'updated')
    list_filter = ('is_available', 'created', 'updated')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'
    ordering = ('-created',)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')
    search_fields = ('product__name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)