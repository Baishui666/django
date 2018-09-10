from django.db import models


class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True)
    o_user = models.ForeignKey('tt_user.UserInfo')
    o_date = models.DateTimeField(auto_now=True)
    o_isPay = models.BooleanField(default=False)
    o_total = models.DecimalField(max_digits=6, decimal_places=2)
    oaddress = models.CharField(max_length=150)


class Orderlist(models.Model):
    goods = models.ForeignKey('tt_goods.GoodsInfo')
    order = models.ForeignKey('OrderInfo')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()
