from django.contrib import admin

from webapp.models import Categories, Products

# Register your models here.

class Categories_Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    fields = ('title', 'description')

admin.site.register(Categories, Categories_Admin)


class Products_Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'price', 'image')
    list_filter = ('id', 'title', 'description', 'category', 'price', 'image')
    search_fields = ('title', 'description', 'category', 'price')
    fields = ('title', 'description', 'category', 'price', 'image')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Products, Products_Admin)