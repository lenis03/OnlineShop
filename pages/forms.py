from django import forms

from .models import ContactUS


class ContactUsForms(forms.ModelForm):
    class Meta:
        models = ContactUS
        fields = ['name', 'email', 'phone_number', 'message', ]