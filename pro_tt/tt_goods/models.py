from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    t_title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    class Meta():
        ordering = ['id']

    def __str__(self):
        return self.t_title.encode('utf-8')


class GoodsInfo(models.Model):
    g_title = models.CharField(max_length=20)
    g_pic = models.ImageField(upload_to='tt_goods')
    g_price = models.DecimalField(max_digits=5, decimal_places=2)
    g_unit = models.CharField(max_length=10,default='500g')
    g_intro = models.CharField(max_length=100)
    g_content = HTMLField()
    g_click = models.IntegerField()
    g_stock = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    g_type = models.ForeignKey('TypeInfo')

    class Meta():
        ordering = ['id']

    def __str__(self):
        return self.g_title.encode('utf-8')