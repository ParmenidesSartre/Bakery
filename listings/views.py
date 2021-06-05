from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from menu.models import Menu
from cart.forms import CartAddProductForm

def vault(request):
    query = request.GET.get('q')
    if query:
        menus = Menu.objects.filter(name__icontains=query)
    else:
        menus =  Menu.objects.order_by('-added_on').all()
    
    paginator = Paginator(menus, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'menus' : paged_listings
    }

    return render(request, 'pages/product-listing.html', context)

def cupcake(request, listing_id):
    listing = get_object_or_404(Menu, pk=listing_id)
    cart_product_form = CartAddProductForm()
    context = {
        'listing' : listing,
        'cart_product_form': cart_product_form
    }

    return render(request, 'pages/product-detail.html', context )
