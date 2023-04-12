from django.contrib import admin

from .models import Products, Comment


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    model = Products
    list_display = ['title', 'price', 'active', 'datetime_modified']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['author', 'body', 'product', 'stars', 'is_active', 'datetime_modified']


