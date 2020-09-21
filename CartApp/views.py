from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from CartApp.models import SxsdCart


def cart(request):
    u_id = request.session.get('user_id')
    if u_id:
        carts = SxsdCart.objects.filter(c_user_id=u_id)
        is_not_all_select = carts.filter(c_is_select=False).exists()
        # True 不是全选
        # False  全选
        context = {
            'carts': carts,
            'is_not_all_select': is_not_all_select,
            'total_price': get_total_price(u_id)
        }
        return render(request, 'sxsd/main/cart/cart.html', context=context)
    else:
        return redirect(reverse('sxsduser:login'))


#  添加购物车
def addToCart(request):
    u_id = request.session.get('user_id')
    if u_id:
        g_id = request.GET.get('g_id')
        carts = SxsdCart.objects.filter(c_goods_id=g_id, c_user_id=u_id)
        if carts.count():
            cart = carts[0]
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = SxsdCart()
            cart.c_goods_num = 1
            cart.c_goods_id = g_id
            cart.c_user_id = u_id
            cart.c_is_select = True
        cart.save()
        data = {
            'msg': 'ok',
            'status': 200,
            'c_goods_num': cart.c_goods_num
        }
        return JsonResponse(data=data)
    else:
        return redirect(reverse('sxsduser:login'))


#  从购物车中减少
def reduceFromCart(request):
    u_id = request.session.get('user_id')
    if u_id:
        g_id = request.GET.get('g_id')
        print(g_id)
        carts = SxsdCart.objects.filter(c_goods_id=g_id, c_user_id=u_id)
        if carts.count():
            cart = carts[0]
            cart.c_goods_num = cart.c_goods_num - 1
            if cart.c_goods_num == 0:
                print(1)
                cart.delete()
                data = {
                    'msg': 'ok',
                    'status': 200,
                }
                return JsonResponse(data=data)
            else:
                print(2)
                cart.save()
                data = {
                    'msg': 'ok',
                    'status': 200,
                    'c_goods_num': cart.c_goods_num
                }
                return JsonResponse(data=data)
        else:
            data = {
                'msg': 'ok',
                'status': 200,
            }
            return JsonResponse(data=data)
    else:
        return redirect(reverse('sxsduser:login'))


#  修改购物车中的数量
def modifyGoodsNum(request):
    cartid = request.GET.get('cartid')
    u_id = request.session.get('user_id')
    add_reduce = request.GET.get('add_reduce')
    cart = SxsdCart.objects.get(pk=cartid)
    if add_reduce == 'add':
        cart.c_goods_num += 1
        cart.save()
    else:
        if cart.c_goods_num == 1:
            cart.delete()
            data = {
                'msg': 'ok',
                'status': 200,
                'total_price': get_total_price(u_id)
            }
            return JsonResponse(data=data)
        else:
            cart.c_goods_num -= 1
            cart.save()
    data = {
        'msg': 'ok',
        'status': 200,
        'c_goods_num': cart.c_goods_num,
        'total_price': get_total_price(u_id)
    }
    return JsonResponse(data=data)


#  单选状态改变
def select(request):
    cartid = request.GET.get('cartid')
    cart = SxsdCart.objects.get(pk=cartid)
    cart.c_is_select = not cart.c_is_select
    cart.save()
    u_id = request.session.get('user_id')
    is_not_all_select = SxsdCart.objects.filter(c_user_id=u_id).filter(c_is_select=False).exists()
    data = {
        'msg': 'ok',
        'status': 200,
        'c_is_select': cart.c_is_select,
        'is_not_all_select': is_not_all_select,
        'total_price': get_total_price(u_id)
    }
    return JsonResponse(data=data)


#  全选状态改变
def allselect(request):
    all_select_list = request.GET.get('all_select_list')
    all_select_list = all_select_list.split("#")

    carts = SxsdCart.objects.filter(id__in=all_select_list)
    for cart in carts:
        cart.c_is_select = not cart.c_is_select
        cart.save()
    u_id = request.session.get('user_id')
    data = {
        'msg': 'ok',
        'status': 200,
        'total_price': get_total_price(u_id)

    }
    return JsonResponse(data=data)


#  获取总计价格
def get_total_price(user_id):
    total_price = 0
    carts = SxsdCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)
    for cart in carts:
        total_price += cart.c_goods_num * cart.c_goods.price
    return round(total_price, 2)
