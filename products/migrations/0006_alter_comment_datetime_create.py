# Generated by Django 4.0.2 on 2023-05-16 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]