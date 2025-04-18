from django.contrib import admin
from .models import Product 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','price','stock','category','modified','is_available')
    list_display_links = ('product_name',)
    prepopulated_fields = {'slug':('product_name',)}


admin.site.register(Product,ProductAdmin)
