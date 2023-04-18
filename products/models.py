from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


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


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(is_active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
        ]

    body = models.TextField(verbose_name=_('comment text'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='comment author')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments')
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('Whats Your Score?'))

    # Manager
    object = models.Manager()
    active_comment_manager = ActiveCommentManager()

    def __str__(self):
        return f'{self.author}:{self.body}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])


# Comment.object.all.filter(is_active=True)
# Comment.active_comment_manager.all()
    