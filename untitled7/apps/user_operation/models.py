from django.db import models
from apps.goods.models import Goods
from apps.user.models import User
from datetime import datetime
# Create your models here.
class GoodsFar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", help_text="商品id")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    province = models.CharField("省份", max_length=100, default="")
    city = models.CharField("城市", max_length=100, default="")
    district = models.CharField("区域", max_length=100, default="")
    address = models.CharField("详细地址", max_length=100, default="")
    signer_name = models.CharField("签收人", max_length=100, default="")
    signer_mobile = models.CharField("电话", max_length=11, default="")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
