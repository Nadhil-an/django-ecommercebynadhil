from django.contrib import admin
from .models import Cart,CartItem
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id','date_add')


admin.site.register(Cart,CartAdmin)