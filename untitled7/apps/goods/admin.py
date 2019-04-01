from django.contrib import admin


from  .models import  Goods,BannerLBT,ShopBanner

class GoodsAdmin(object):
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]
    style_fields = {"goods_desc": "ueditor"}

class LBTAdmin(object):
    list_display = ['active','images','goods']

class ShopAdmin(object):
    list_display = ['images', 'goods']


import xadmin
xadmin.site.register(Goods,GoodsAdmin)
xadmin.site.register(BannerLBT,LBTAdmin)
xadmin.site.register(ShopBanner,ShopAdmin)
