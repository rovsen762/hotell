
from django.contrib import admin
from .models import Hotel, Variation, HotelGallery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class HotelGalleryInline(admin.TabularInline):
    model = HotelGallery
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [HotelGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('hotel', 'variation_category', 'variation_value')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(HotelGallery)




