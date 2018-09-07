#coding=utf-8

from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hashlib import sha1
from models import *
import user_decorator
import user


def register(request):
    context = {'title': '注册'}
    return render(request, 'tt_user/register.html', context)


def register_handle(request):

    # 接受注册表单信息
    uname = request.POST['user_name']
    pwd1 = request.POST['pwd']
    pwd2 = request.POST['cpwd']
    uemail = request.POST['email']

    if uname == '' or pwd1 == '' or pwd2 == '':
        return redirect('/user/register/')

    # 判断两次密码是否一致
    if pwd1 != pwd2:
        return redirect('/user/register/')

    # 密码sha1加密
    s1 = sha1()
    s1.update(pwd1)
    upwd = s1.hexdigest()

    # 向数据库插入数据
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uemail = uemail
    user.save()

    response = HttpResponseRedirect('/user/login/')
    response.set_cookie('uname', uname)
    return response


def user_exists(request):
    name = request.GET.get('username')
    count = UserInfo.objects.filter(uname=name).count()

    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')

    context = {'title': '登录', 'erorr_name': 0, 'erorr_pwd': 0, 'uname': uname}
    return render(request, 'tt_user/login.html', context)


def login_handel(request):

    # 接收登录信息
    uname = request.POST['username']
    pwd = request.POST['pwd']
    pwd_record = request.POST.get('pwd_record', '0')

    # 判断用户合法性
    user = UserInfo.objects.filter(uname=uname)     # 返回[object1, object2]

    if len(user) == 1:
        s1 = sha1()
        s1.update(pwd)
        upwd = s1.hexdigest()

        if upwd == user[0].upwd:

            # 判断是否从其他等转向过来的登录，通过取session['url']，如果非空，验证通过后返回原来url页面
            url = request.COOKIES.get('url', '/')
            print '11111', url
            response = HttpResponseRedirect(url)

            if pwd_record == '1':
                response.set_cookie('uname', uname)
            else:
                response.set_cookie('uname', '', max_age=-1)

            # 登录成功，设置session id,name
            request.session['user_id'] = user[0].id
            request.session['user_name'] = uname

            return response

        else:
            context = {'title': '登录', 'erorr_name': 0, 'erorr_pwd': 1, 'uname': uname, 'pwd': pwd, 'pwd_record': pwd_record}
            return render(request, 'tt_user/login.html', context)
    else:
        context = {'title': '登录', 'erorr_name': 1, 'erorr_pwd': 0, 'uname': uname, 'pwd': pwd, 'pwd_record': pwd_record}
        return render(request, 'tt_user/login.html', context)


def logout(request):
    request.session.flush()
    return redirect('/')


@user_decorator.login_check
def info(request):
    user_id = request.session.get('user_id', default='')
    uname = request.session.get('user_name', default='')
    user = UserInfo.objects.filter(id=user_id)

    # 取COOKIES上goods id的浏览记录值，然后进行遍历，构造最新的5条数据列表至html渲染
    goods_record = request.COOKIES.get('goods_record', '')
    goods_list = []
    if goods_record != '':
        gids = goods_record.split(',')
        for gid  in gids:
            goods = GoodsInfo.objects.get(id=int(gid))
            goods_list.append(goods)

    context = {'title': '用户中心',
               'page_name': 1,
               'uname': uname,
               'email': user[0].uemail,
               'goods_list': goods_list}

    return render(request, 'tt_user/user_center_info.html', context)


@user_decorator.login_check
def order(request):
    context = {'page_name': 1}
    return render(request, 'tt_user/user_center_order.html', context)


@user_decorator.login_check
def site(request):
    user_id = request.session.get('user_id')

    user = UserInfo.objects.get(id=user_id)
    if request.method == 'POST':

        user.ureceive = request.POST['recieve']
        user.uaddress = request.POST['address']
        user.postcode = request.POST['postcode']
        user.uphone = request.POST['phone']
        user.save()

    context = {'title': '用户中心', 'page_name': 1, 'user': user}
    return render(request, 'tt_user/user_center_site.html', context)




















