from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

from cart.cart import Cart


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(_('Is Paid?'), default=False)

    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    phone_number = PhoneNumberField(_('Phone Number'))
    address = models.CharField(_('Address'), max_length=700)
    order_note = models.CharField(_('Order Note'), max_length=1000, blank=True)

    zarinpal_authority = models.CharField(max_length=255, blank=True)
    zarinpal_ref_id = models.CharField(max_length=150, blank=True)
    zarinpal_data = models.TextField(blank=True)

    datetime_created = models.DateTimeField(_('Created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Modified'), auto_now=True)

    def __str__(self):
        return f'order: {self.id}'

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())

    def return_products_to_cart(self, request):
        cart = Cart(request)
        rec_cart = None
        for item in self.items.all():
            rec_cart = cart.add(item.product, item.quantity)
        return rec_cart


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'(order_item: {self.id}), ({self.product} * {self.quantity}), (price: {self.price}),' \
               f' (order: {self.order.id})'
