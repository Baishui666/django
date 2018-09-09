#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from models import *
import user_decorator


def index(request):
    typelist = TypeInfo.objects.all()

    # 获取最近上架的商品，即id靠后;获取最多点击的，g_click最多的
    fruit_new = typelist[0].goodsinfo_set.order_by('-id')[0: 4]
    fruit_click = typelist[0].goodsinfo_set.order_by('-g_click')[0: 4]

    seafood_new = typelist[1].goodsinfo_set.order_by('-id')[0: 4]
    seafood_click = typelist[1].goodsinfo_set.order_by('-g_click')[0: 4]

    meat_new = typelist[2].goodsinfo_set.order_by('-id')[0: 4]
    meat_click = typelist[2].goodsinfo_set.order_by('-g_click')[0: 4]

    egg_new = typelist[3].goodsinfo_set.order_by('-id')[0: 4]
    egg_click = typelist[3].goodsinfo_set.order_by('-g_click')[0: 4]

    vegetable_new = typelist[4].goodsinfo_set.order_by('-id')[0: 4]
    vegetable_click = typelist[4].goodsinfo_set.order_by('-g_click')[0: 4]

    ice_new = typelist[5].goodsinfo_set.order_by('-id')[0: 4]
    ice_click = typelist[5].goodsinfo_set.order_by('-g_click')[0: 4]

    context = {'title': '首页', 'guest_car': 1 ,
               'fruit_new': fruit_new, 'fruit_click': fruit_click,
               'seafood_new': seafood_new, 'seafood_click': seafood_click,
               'meat_new': meat_new, 'meat_click': meat_click,
               'egg_new': egg_new, 'egg_click': egg_click,
               'vegetable_new': vegetable_new, 'vegetable_click': vegetable_click,
               'ice_new': ice_new, 'ice_click': ice_click,
               }

    return render(request, 'tt_goods/index.html', context)


def list(request, tid, pindex, sort):   # type_id, 第几页， 排序类型
    # 获取商品类型
    g_type = TypeInfo.objects.get(pk=int(tid))
    goods_new = g_type.goodsinfo_set.order_by('-id')[0:2]        # 按照最新商品排序，id靠后

    goods = []
    if sort == '1':
        goods = GoodsInfo.objects.filter(g_type_id=int(tid)).order_by('-id')      # 默认排序

    if sort == '2':
        goods = GoodsInfo.objects.filter(g_type_id=int(tid)).order_by('g_price')        # 按照点击量最多的排序，即人气

    if sort == '3':
        goods = GoodsInfo.objects.filter(g_type_id=int(tid)).order_by('-g_click')     # 按照价格最低的排序

    paginator = Paginator(goods, 10)

    goods_page = paginator.page(int(pindex))

    context = {'title': '商品列表', 'guest_car': 1,
               'g_type': g_type,
               'goods_new': goods_new,
               'paginator': paginator,
               'goods_page': goods_page,
               'sort': sort,

               }

    return render(request, 'tt_goods/list.html', context)


def detail(request, gid):       # 提供good_id参数

    goods = GoodsInfo.objects.get(pk=int(gid))
    goods.g_click = goods.g_click + 1
    g_type = goods.g_type
    new_goods = GoodsInfo.objects.filter(g_type_id=int(g_type.id)).order_by('-id')[0:2]
    context = {'title': '商品列表', 'guest_car': 1,
               'g_type': g_type, 'goods': goods,
               'new_goods': new_goods,
               }
    # render也是调用HttpResponse类
    response = render(request, 'tt_goods/detail.html', context)

    # 判断COOKIES是否有保存浏览记录，默认为空，如果为空，则是用户第一次浏览goods详情页面
    goods_record = request.COOKIES.get('goods_record', '')

    if goods_record == '':
        response.set_cookie('goods_record', gid)
    else:
        record_list = goods_record.split(',')
        # 判断是否浏览过该页面，有则先删除记录，再添加至最前面
        if gid in record_list:
            record_list.remove(gid)
            record_list.insert(0, gid)

        else:
            record_list.insert(0, gid)
        # 判断记录列表是否大于5条，则删除最后一条
        if len(record_list) > 5:
            del record_list[-1]

        # 构造goods_cookie的值为'gid1,gid2,gid3...'格式
        response.set_cookie('goods_record', ','.join(record_list))

    return response