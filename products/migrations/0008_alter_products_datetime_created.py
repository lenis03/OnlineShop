# Generated by Django 4.0.2 on 2023-05-16 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_comment_datetime_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time of Creation'),
        ),
    ]
