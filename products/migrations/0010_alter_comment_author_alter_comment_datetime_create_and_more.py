# Generated by Django 4.0.2 on 2023-06-07 11:22

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_products_short_description_alter_products_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Comment Author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت '),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ اخرین تغییر'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.products', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='products',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='products',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ساخت '),
        ),
        migrations.AlterField(
            model_name='products',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ اخرین تغییر'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='جزئیات محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='product/product_cover', verbose_name='عکس محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.PositiveIntegerField(verbose_name='قیمت '),
        ),
        migrations.AlterField(
            model_name='products',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='جزئیات کوتاه برای محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
    ]
