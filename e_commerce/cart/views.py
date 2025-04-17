from django.shortcuts import render,redirect
from .models import Cart,CartItem
from store.models import Product

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart



def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.object.get(id=product_id)

    try:
        cart = Cart.objects.get(card_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity =+ 1
        cart = cart

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,
                                            quantity = 1,
                                            cart=cart)
    return redirect('cart')



# Create your views here.
def cart(request):
    return render(request,'cart.html')