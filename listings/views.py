from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from menu.models import Menu
from cart.cart import Cart
from cart.forms import CartAddProductForm

def vault(request):
    query = request.GET.get('q')
    if query:
        menus = Menu.objects.filter(name__icontains=query)
    else:
        menus = Menu.objects.order_by('added_on').all()
    
    paginator = Paginator(menus, 4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    best_sellers = Menu.objects.filter(best_seller = True)
    new_cakes = Menu.objects.order_by('-added_on')[:3]

    cart = Cart(request)

    context = {
        'menus' : paged_listings,
        'best_sellers' : best_sellers,
        'new_cakes' : new_cakes,
        'cart' : cart
    }

    return render(request, 'pages/product-listing.html', context)

def cupcake(request, name):
    listing = get_object_or_404(Menu, slug=name)
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    context = {
        'listing' : listing,
        'cart_product_form': cart_product_form,
        'cart' : cart
    }

    return render(request, 'pages/product-detail.html', context )
