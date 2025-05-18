from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class AccountAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'is_admin', 'is_staff', 'last_login', 'is_active')
    list_display_links = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    list_filter = ('is_admin',)
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(Account, AccountAdmin)