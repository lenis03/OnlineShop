from django.db import models
from django.utils.translation import gettext as _


from phonenumber_field.modelfields import PhoneNumberField


class ContactUS(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(max_length=254, verbose_name=_('email'))
    phone_number = PhoneNumberField(_('Phone Number'))
    message = models.TextField(verbose_name=_('message'))

    def __str__(self):
        return f'{self.name}'
