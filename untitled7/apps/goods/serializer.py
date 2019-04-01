from .models import Goods,GoodsCategory,BannerLBT,ShopBanner
from rest_framework import serializers
class CategarySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategarySerializer2(serializers.ModelSerializer):
    sub_cat=CategarySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategarySerializer(serializers.ModelSerializer):
    sub_cat=CategarySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class ShopSerialier(serializers.ModelSerializer):
    class Meta:
        model = ShopBanner
        fields = "__all__"
class  GoodsSerializer(serializers.ModelSerializer):
    category = CategarySerializer()
    image=ShopSerialier(many=True)
    class Meta:
        model = Goods
        fields = "__all__"








class LbtSerialier(serializers.ModelSerializer):
    class Meta :
        model = BannerLBT
        fields = "__all__"



