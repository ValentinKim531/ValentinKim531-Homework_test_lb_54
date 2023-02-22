from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Products, Categories


def categories_view(request: WSGIRequest):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories_view.html', context=context)


def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect('categories')


def edit_category(request: WSGIRequest, pk):
    category = get_object_or_404(Categories, pk=pk)
    if request.method == "GET":
        return render(request, 'category_edit_view.html', context={'category': category})
    category.title = request.POST.get('title')
    category.description = request.POST.get('description')
    category.save()
    return redirect('categories')
