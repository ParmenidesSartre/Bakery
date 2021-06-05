from django.shortcuts import render
from menu.models import Menu
from bakers.models import Baker

def index(request):
    best_sellers = Menu.objects.filter(best_seller = True)
    new_cakes = Menu.objects.order_by('-added_on')[:3]
    hot_cakes = Menu.objects.filter(hot_item= True)[:3]

    context = {
        'best_sellers': best_sellers,
        'new_cakes': new_cakes,
        'hot_cakes' : hot_cakes
    }

    return render(request, 'pages/index.html', context)

def about(request):
    baker = Baker.objects.all()[:1]
    baker_team = Baker.objects.all()[:3]

    context = {
        'baker' : baker,
        'baker_team' : baker_team
    }

    return render(request, 'pages/about.html', context )
