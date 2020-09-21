from alipay import AliPay, AliPayConfig
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from CartApp.models import SxsdCart
from CartApp.views import get_total_price
from OrderApp.models import SxsdOrder, SxsdOrderGoods
from UserApp.models import SxsdUser
from sxsd.settings import PRIVATE_KEY, PUBLIC_KEY


def order(request):
    uid = request.session.get('user_id')
    # user = SxsdUser.objects.get(pk=uid)
    order = SxsdOrder()
    order.o_user_id = uid
    order.o_total_price = get_total_price(uid)
    order.save()

    carts = SxsdCart.objects.filter(c_user_id=uid).filter(c_is_select=True)

    for cart in carts:
        orderGoods = SxsdOrderGoods()
        orderGoods.og_order = order
        orderGoods.og_goods = cart.c_goods
        orderGoods.og_c_goods_num = cart.c_goods_num
        orderGoods.save()
        cart.delete()
    # context = {
    #     'order':order
    # }
    return redirect(f'/sxsdorder/orderDetail/?order_id={order.id}')
    # return render(request,'sxsd/order/detail/order_detail.html',context=context)

def orderDetail(request):
    order_id = request.GET.get('order_id')
    order = SxsdOrder.objects.get(pk=order_id)
    time1 = str(order.o_time)
    time2 = time1.split('-')
    time3 = ''
    time4 = time3.join(time2)
    time5 = time4.split(' ')
    time6 = time3.join(time5)
    time7 = time6.split(':')
    o_time = time3.join(time7)
    context = {
        'order':order,
        'o_time':o_time
    }
    return render(request,'sxsd/order/detail/order_detail.html',context=context)


def testPay(request):
    total_price = request.GET.get('total_price')
    alipay = AliPay(
        appid="2016093000627735",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=PRIVATE_KEY,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=PUBLIC_KEY,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = False,  # 默认False
        config = AliPayConfig(timeout=15)  # 可选, 请求超时时间
    )

    subject = "AXF订单支付"

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="110",
        total_amount=total_price,
        subject=subject,
        return_url="http://www.1000phone.com",
        notify_url="http://www.1000phone.com"  # 可选, 不填则使用默认notify url
    )

    # return JsonResponse()
    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)