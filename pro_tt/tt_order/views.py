#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from models import *
from tt_cart.models import *
from tt_user.models import *
from tt_goods.models import *
from datetime import datetime


def order(request):
    # 获取cart购物车的id，并进行数据库查询后保存carts
    carts_id = request.GET.getlist('cart_id')
    print ','.join(carts_id)
    # 第一种写法
    # carts = []
    # for cart_id in carts_id:
    #     cart = CartInfo.objects.get(pk=int(cart_id))
    #     carts.append(cart)

    # 第二种写法
    carts_id1 = [int(cart_id) for cart_id in carts_id]
    carts = CartInfo.objects.filter(pk__in=carts_id1)

    # 获取user_id,并进行数据库查询
    user_id = request.session.get('user_id')
    user = UserInfo.objects.get(pk=user_id)

    context = {
        'title': '订单提交', 'page_name': 1,
        'user': user, 'carts': carts,
        'carts_id': ','.join(carts_id),

    }
    return render(request, 'tt_order/place_order.html', context)


"""
1.创建订单对象
2.判断商品库存
3.创建详单对象
4.修改商品库存
5.删除购物车
"""

@transaction.atomic()
@csrf_exempt
def order_handle(request):
    address = request.POST.get('address')
    tran_id = transaction.savepoint()
    carts_id = request.POST.get('carts_id')

    try:
        order = OrderInfo()
        now = datetime.now()
        uid = request.session.get('user_id')
        order.oid = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), uid)
        order.o_user_id = uid
        order.o_date = now
        order.o_isPay = True
        order.o_total = request.POST.get('total')
        order.save()
        print 'order.save'

        carts_id = [int(cart_id) for cart_id in carts_id.split(',')]
        for cart_id in carts_id:
            detail = Orderlist()

            detail.order = order
            print cart_id
            cart = CartInfo.objects.get(pk=cart_id)
            goods = cart.goods
            if cart.count <= goods.g_stock:
                detail.goods = cart.goods
                detail.price = cart.goods.g_price
                detail.count = cart.count

                detail.save()


                goods.g_stock = goods.g_stock - cart.count
                goods.save()

                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart')
        transaction.savepoint_commit(tran_id)

    except Exception as e:
        print '-------------%s' % e.message
        transaction.savepoint_commit(tran_id)
    else:
        res = HttpResponseRedirect('/user/order/')
        res.set_cookie('count', 0)
        return res





















