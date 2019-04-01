import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled7.settings")
import django
django.setup()
from dbtools.data.product_data import row_data
from apps.goods.models import Goods,GoodsCategory,ShopBanner


def addGoods():
    for  item in row_data:
        name=item['name']
        market_price=float(item['market_price'].replace('元','').replace('￥',''))
        desc=item['desc']
        if not  desc :
            desc=''
        sale_price=float(item['sale_price'].replace('元','').replace('￥',''))
        goods_desc=item['goods_desc']
        images = item['images']
        goods_front_image=item['images'][0]
        category_name=item['categorys'][-1]
        category=GoodsCategory.objects.filter(name=category_name).first()
        Goods.objects.create(category=category,name=name,market_price=market_price,shop_price=sale_price,
        goods_desc=desc,
                             goods_front_image=goods_front_image                     )


def  Banner():
    for   i  in range(1,53):
        item=Goods.objects.filter(id=i).first()
        ShopBanner.objects.create(goods=item,images='goods/banner/goods/banner/720333-20180329153803371-1547553579_7oKPpsH.png')


addGoods()
Banner()