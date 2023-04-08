from django.contrib import admin

from .models import Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    model = Products
    list_display = ['title', 'price', 'active', 'datetime_modified']

