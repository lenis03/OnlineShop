from django.shortcuts import render, get_object_or_404, redirect
from config import settings
import requests
import json
from django.http import HttpResponse

from orders.models import Order


def payment_process(request):
    # Get order id from session
    order_id = request.session['order_id']
    # Get the order object
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = 'https://api.zarinpal.com/pg/v4/payment/request.json'

    request_header = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    request_data = {
        'merchant_id': settings.ZARINPALL_MERCHANT_ID,
        'amount': rial_total_price,
        'description': f'#{order_id} : {order.user.first_name} {order.user.last_name}',
        'callback_url': 'http://127.0.0.1:8000',
    }

    res = requests.post(zarinpal_request_url, data=json.dumps(request_data), headers=request_header)

    # print(res.json()['data'])

    data = res.json()['data']
    authority = data['authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}')
    else:
        return HttpResponse('Error from zarinpal')


