from django.contrib import admin
from .models import ShopCar


class  ShopCarAdmin(object):
    list_display = ['user', 'goods', 'id','nums']



import xadmin
xadmin.site.register(ShopCar,ShopCarAdmin)