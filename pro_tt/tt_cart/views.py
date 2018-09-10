#coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from models import *
from tt_goods.models import *
from tt_goods import user_decorator


@user_decorator.login_check
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    if carts.count() == 0:
        state = 0
    else:
        state = 1

    context = {
        'title': '购物车',
        'page_name': 1,
        'carts': carts,
        'state': state,
    }
    return render(request, 'tt_cart/cart.html', context)


@user_decorator.login_check
def add(request, gid, count):

    cookie_count = request.COOKIES['count']
    print 'cookie_count', cookie_count
    res = HttpResponseRedirect('/cart')

    uid = request.session['user_id']
    uid = int(uid)
    gid = int(gid)
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    # 判断添加的商品是否在cart上，是的话在count+1,否则新生成一行数据并更新cookie中count加1
    if len(carts) >= 1:
        print '商品已添加'
        carts[0].count = carts[0].count + int(count)
        carts[0].save()
        state = 0
    else:
        print '商品未添加'
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = int(count)
        cart.save()
        state = 1

        res.set_cookie('count', int(cookie_count) + 1)
        print 'set_cookie成功', int(cookie_count) + 1

    # 如果是ajax请求则返回json格式
    if request.is_ajax():
        if state == 1:
            count = CartInfo.objects.filter(user_id=uid).count()
            jres = JsonResponse({'count': count})
            jres.set_cookie('count', int(count))
            print 'ajax:count', count
        else:
            jres = JsonResponse({'count': 0})
            print 'count: 0'
        return jres

    return res


def edit(request, cid, count):
    cid = int(cid)
    try:
        cart = CartInfo.objects.get(id=cid)
        cart.count = count
        cart.save()
    except:
        state = 0
    else:
        state =1

    return JsonResponse({'state': state})


def delete(request, cid):
    cid = int(cid)
    num = 0
    try:
        cart = CartInfo.objects.get(pk=cid)

        cart.delete()
    except:
        status = 0
        print '删除失败'
    else:
        status = 1
        num = 1
        print '删除成功'

    res = JsonResponse({'status': status})
    # count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
    count = request.COOKIES['count']

    res.set_cookie('count', int(count) - num)
    print 'cookies设置成功'

    return res


