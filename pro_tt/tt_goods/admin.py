from django.contrib import admin
from models import *


@admin.register(TypeInfo)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 't_title']


@admin.register(GoodsInfo)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'g_title', 'g_price', 'g_unit', 'g_click','g_type']
    list_per_page = 5