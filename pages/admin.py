from django.contrib import admin
from .models import ContactUS


@admin.register(ContactUS)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUS
    list_display = ['name', 'email', 'phone_number', ]
