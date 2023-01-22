from django.contrib import admin
from .models import Order, OrderHotel

class OrderHotelInline(admin.TabularInline):
    model = OrderHotel
    readonly_fields = ('user','hotel')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_filter = ('is_ordered', 'order_begin_date')
    search_fields = ('order_number', 'first_name', 'last_name', 'phone', 'email', 'person_number', 'order_begin_date', 'order_end_date', 'order_note')
    list_per_page = 20
    inlines = [OrderHotelInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderHotel)

