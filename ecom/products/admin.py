from django.contrib import admin
from .models import *
# Register your models here .                                                          

admin.site.register(Category)

# Add Images in product table

class ProductImageAdmin(admin.StackedInline):
    model=ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "price" ]
    inlines=[ProductImageAdmin]


@admin.register(SizeVariant)
class SizeVarientAdmin(admin.ModelAdmin):
    list_display = ["size_name","price"]
    model = SizeVariant


@admin.register(ColorVariant)
class ColorVarientAdmin(admin.ModelAdmin):
    list_display = ["color_name","price"]
    model = ColorVariant

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)