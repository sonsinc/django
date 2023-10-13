from django.contrib import admin
from app_gen.models import Product

class ManageProduct(admin.ModelAdmin):
    list_display = ['name', 'price','stock','trending']
    list_editable = ['price', 'stock', 'trending']
    list_per_page = 6
    search_fields = ['name']
    list_filter = ['trending']

# Register your models here.
admin.site.register(Product, ManageProduct)