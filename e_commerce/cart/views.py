from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart,CartItem
from store.models import Product



def _cart_id(request):
    session_key = request.session.session_key
    if not session_key:
        session_key = request.session.create()
    return session_key


def add_cart(request,product_id):
    my_product = Product.objects.get(id=product_id)

    session_key = _cart_id(request)
    try:
        cart = Cart.objects.get(cart_id = session_key)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = session_key)
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=my_product,cart=cart)
        cart_item.quantity += 1
        cart = cart
        cart_item.save()
        
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=my_product,
                                            quantity = 1,
                                            cart=cart)
    return redirect('cart')

# quantity decrement

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id =_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


# removing product from the cart

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_items = CartItem.objects.get(product=product,cart=cart)
    cart_items.delete()
    return redirect('cart')




def cart(request, total=0, quantity=0, cart_item=None):
    
    session_key = _cart_id(request) 
    cart = Cart.objects.get(cart_id=session_key)   
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    
    for cart_item in cart_items:   
        item_total = cart_item.quantity * cart_item.product.price
        cart_item.total = item_total  
        total += item_total  
        quantity += cart_item.quantity
    tax = (2 * total)/100
    grant_total = total+tax
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'grant_total' :grant_total,
        'tax':tax
    }
    
    return render(request, 'cart.html', context)
