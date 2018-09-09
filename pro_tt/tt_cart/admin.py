from django.contrib import admin
from models import *

@admin.register(CartInfo)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'goods', 'count']
