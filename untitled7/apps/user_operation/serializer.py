from rest_framework import serializers
from  .models import  GoodsFar,UserAddress
from rest_framework.validators import UniqueTogetherValidator
from apps.goods.serializer import GoodsSerializer
class GoodsFarSer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault ()# 当前用户
    )
    class Meta:
        model = GoodsFar
        validators = [
            UniqueTogetherValidator(
                queryset=GoodsFar.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]
        fields = '__all__'

class UserGoodsFarSer(serializers.ModelSerializer):
    goods=GoodsSerializer()
    class Meta:
        model = GoodsFar
        fields = ('id', 'goods')

class UserAddresserializers(serializers.ModelSerializer):
    # 不需要提交
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()  # 当前用户
    )
    class Meta:
        model = UserAddress
        fields = "__all__"
