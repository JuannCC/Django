from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","short_description","stock",)
    search_fields= ("name","short_description",)
    list_filter= ("discount_unitl",)
    date_hierachy= "discount_unitl"

admin.site.register(Product, ProductAdmin)