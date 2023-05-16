# Generated by Django 4.0.2 on 2023-05-16 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_comment_datetime_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
