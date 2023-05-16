from django.contrib import admin

from .models import Products, Comment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentInline(admin.StackedInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'is_active']
    extra = 1


@admin.register(Products)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    model = Products
    list_display = ['title', 'price', 'active', 'datetime_modified']

    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['author', 'body', 'product', 'stars', 'is_active', 'datetime_modified']


