from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from webapp.models import Products, Categories


def product_add_view(request: WSGIRequest):
    if request.method == "GET":
        categories = Categories.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'product_add.html', context=context)


    product_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'category_id': request.POST.get('category_id'),
        'price': request.POST.get('price'),
        'image': request.POST.get('image')
    }
    product = Products.objects.create(**product_data)
    return redirect('product_view', pk=product.pk)
