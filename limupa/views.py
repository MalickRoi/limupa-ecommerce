from django.shortcuts import render
from store.models import Product

def home_view(request):
    products = Product.objects.filter(is_available=True)
    context = {
        'title': 'Home',
        'products': products,
    }
    return render(request, 'home.html', context)

