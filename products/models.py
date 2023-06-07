from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils import timezone

from ckeditor.fields import RichTextField


class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    short_description = models.TextField(blank=True, verbose_name=_('Short_description'))
    price = models.PositiveIntegerField(verbose_name=_('Price'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='product/product_cover')

    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('Date Time of Creation'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date Time of Modified'))

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
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('Comment Author'))
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Product'))
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Time of Creation'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date Time of Modified'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
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
    