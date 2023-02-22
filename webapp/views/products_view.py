from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.models import Products


def products_view(request: WSGIRequest):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)
