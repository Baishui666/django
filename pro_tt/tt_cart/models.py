from django.db import models



class CartInfo(models.Model):
    user = models.ForeignKey('tt_user.UserInfo')
    goods = models.ForeignKey('tt_goods.GoodsInfo')
    count = models.IntegerField()

    def __str__(self):
        return self.user.uname

    class Meta():
        ordering = ['id']