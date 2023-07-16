from django.views import generic
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from pages.models import ContactUS
from pages.forms import ContactUsForms


class ContactUsCreatView(SuccessMessageMixin, generic.CreateView):
    model = ContactUS
    success_message = _("Your message has been successfully sent! ")
    fields = ['name', 'email', 'phone_number', 'message', ]
    template_name = 'pages/contactus.html'
    success_url = reverse_lazy('product_list')
