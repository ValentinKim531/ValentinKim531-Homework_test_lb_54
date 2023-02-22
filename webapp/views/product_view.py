from django.shortcuts import render, get_object_or_404, redirect
from django.core.handlers.wsgi import WSGIRequest

from webapp.models import Products, Categories

def product_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product_view.html', context={
        'product': product
    })


def delete_product(request, pk):
    to_do = get_object_or_404(Products, pk=pk)
    to_do.delete()
    return redirect('products')


def edit_product(request: WSGIRequest, pk):
    product = get_object_or_404(Products, pk=pk)
    categories = Categories.objects.all()
    if request.method == "GET":
        return render(request, 'product_edit_view.html', context={'product': product, 'categories': categories})

    product.title = request.POST.get('title')
    product.description = request.POST.get('description')
    product.category_id = request.POST.get('category_id')
    product.price = request.POST.get('price')
    product.image = request.POST.get('image')
    product.save()
    return redirect('products')

