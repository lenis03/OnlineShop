from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
        ]

    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments')
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS)

    def __str__(self):
        return f'{self.author}:{self.body}'
    