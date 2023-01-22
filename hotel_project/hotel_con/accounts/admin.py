from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone', 'date_joined', 'last_login')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone')
    readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ('email', 'username', 'first_name', 'last_name', 'phone')
    