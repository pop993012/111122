from  .models import  Goods

class GoodsAdmin(object):
    pass


import xadmin
xadmin.site.register(Goods,GoodsAdmin)


