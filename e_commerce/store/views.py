from django.shortcuts import render,get_object_or_404
from . models import Product
from catergory.models import Category
from cart.views import add_cart,CartItem,_cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.

def store(request, category_slug =None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True)
        paginator  =Paginator(products,6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by()
        paginator  =Paginator(products,6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()


    context = {
        'products':paged_products,
        'product_count':product_count
        
    }
    return render(request,'store.html',context)



def product_details(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Product.DoesNotExist:
        # You can show a 404 page instead of crashing the server
        single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    context = {
        'single_product': single_product,
        'in_cart'       : in_cart
    }
    return render(request, 'product_details.html', context)

from django.shortcuts import render
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator

def search(request):

    #getting the keyword value from the url
    keyword = request.GET.get('keyword', '')
    products = []
    

    #if keyword is available getting the products from the database based on product name and product description
    if keyword:
        products = Product.objects.filter(
            Q(description__icontains=keyword) |
            Q(product_name__icontains=keyword)
        ).order_by('-created_date')
#by searching the each page 6 products should be display
    paginator = Paginator(products, 6)  # Show 6 products per page
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'product_count': products.count(),
        'product_number': int(page) if page else 1,
    }
    return render(request, 'store.html', context)
