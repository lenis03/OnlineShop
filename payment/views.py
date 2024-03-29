from django.shortcuts import render, get_object_or_404, redirect, reverse
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
        'callback_url': request.build_absolute_uri(reverse('payment:payment_callback')),
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


def payment_callback(request):
    payment_authority = request.GET.get('Authority')
    payment_status = request.GET.get('Status')
    order = get_object_or_404(Order, zarinpal_authority=payment_authority)
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    if payment_status == 'OK':

        request_header = {
            "accept": "application/json",
            "content-type": "application/json",
        }

        request_data = {
            'merchant_id': settings.ZARINPALL_MERCHANT_ID,
            'amount': rial_total_price,
            'authority': payment_authority,
        }

        res = requests.post(
            'https://api.zarinpal.com/pg/v4/payment/verify.json',
            data=json.dumps(request_data),
            headers=request_header,

        )

        if 'data' in res.json() and ('errors' not in res.json()['data'] or len(res.json()['data']['errors'] == 0)):
            data = res.json()['data']
            payment_code = data['code']
            if payment_code == 100:
                order.is_paid = True
                order.zarinpal_ref_id = data['ref_id']
                order.zarinpal_data = data
                order.save()

                return HttpResponse('پرداخت شما با موفقیت انجام شد!')

            elif payment_code == 101:
                return HttpResponse('پرداخت شما با موفقیت انجام شد.البته این تراکنش قبلا ثبت شده!')

            else:
                order.return_products_to_cart(request)
                error_code = res.json()['errors']['code']
                error_message = res.json()['errors']['message']
                return HttpResponse(f'تراکنش ناموفق بود! {error_message} {error_code} ')

    else:
        order.return_products_to_cart(request)
        return HttpResponse('تراکنش ناموفق بود! ')


def payment_process_sandbox(request):
    # Get order id from session
    order_id = request.session['order_id']
    # Get the order object
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = 'https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json'

    request_header = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    request_data = {
        'MerchantID': 'aaabbbaaabbbaaabbbaaabbbaaabbbaaabbb',
        'Amount': rial_total_price,
        'Description': f'#{order_id} : {order.user.first_name} {order.user.last_name}',
        'CallbackURL': request.build_absolute_uri(reverse('payment:payment_callback')),
    }

    res = requests.post(zarinpal_request_url, data=json.dumps(request_data), headers=request_header)
    print(res)
    # print(res.json()['data'])

    data = res.json()
    print(data)
    authority = data['Authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect(f'https://sandbox.zarinpal.com/pg/StartPay/{authority}')
    else:
        print(data['errors'])
        return HttpResponse('Error from zarinpal')


def payment_callback_sandbox(request):
    payment_authority = request.GET.get('Authority')
    payment_status = request.GET.get('Status')
    order = get_object_or_404(Order, zarinpal_authority=payment_authority)
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    if payment_status == 'OK':

        request_header = {
            "accept": "application/json",
            "content-type": "application/json",
        }

        request_data = {
            'MerchantID': settings.ZARINPALL_MERCHANT_ID,
            'Amount': rial_total_price,
            'Authority': payment_authority,
        }

        res = requests.post(
            'https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json',
            data=json.dumps(request_data),
            headers=request_header,

        )
        print(res.json())
        if 'errors' not in res.json():
            data = res.json()
            payment_code = data['Status']
            if payment_code == 100:
                order.is_paid = True
                order.zarinpal_ref_id = data['RefID']
                order.zarinpal_data = data
                order.save()

                return HttpResponse('پرداخت شما با موفقیت انجام شد!')

            elif payment_code == 101:
                return HttpResponse('پرداخت شما با موفقیت انجام شد.البته این تراکنش قبلا ثبت شده!')

            else:
                order.return_products_to_cart(request)
                error_code = res.json()['errors']['code']
                error_message = res.json()['errors']['message']
                return HttpResponse(f'تراکنش ناموفق بود! {error_message} {error_code} ')

    else:
        order.return_products_to_cart(request)
        return HttpResponse('تراکنش ناموفق بود! ')
