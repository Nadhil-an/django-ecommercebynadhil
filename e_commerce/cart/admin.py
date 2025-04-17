from django.contrib import admin
from .models import Cart,CartItem
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id','date_add')

class Cartitem(admin.ModelAdmin):
    list_display = ('product.product_name','quantity')


admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,Cartitem)