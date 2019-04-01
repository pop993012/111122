from rest_framework import serializers
from .models import ShopCar,OrderGoods
from apps.goods.serializer import GoodsSerializer
from .models import OrderInfo
from random import Random
import time

class ShopCarSerializers(serializers.ModelSerializer):
    goods = GoodsSerializer()
    class Meta:
        model = ShopCar
        fields = "__all__"

class PostShopCarSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = ShopCar
        fields = "__all__"

class OrderInfoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    order_sn = serializers.CharField(read_only=True)
    nonce_str = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    pay_status = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    alipay_url = serializers.SerializerMethodField(read_only=True)

    def get_alipay_url(self, obj):
        from trade.util.aliPay import AliPay
        alipay = AliPay(
            # 沙箱里面的appid值
            appid="2016092000553304",
            # notify_url是异步的url
            app_notify_url="http://http://47.105.128.181:8000/alipay/return/",
            # 我们自己商户的密钥的路径
            app_private_key_path="apps/trade/keys/a.txt",
            # 支付宝的公钥
            alipay_public_key_path="apps/trade/keys/zfb.txt",  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            # debug为true时使用沙箱的url。如果不是用正式环境的url
            debug=True,  # 默认False,
            return_url="http://47.105.128.181:8000/alipay/return/"
        )

        url = alipay.direct_pay(
            # 订单标题
            subject=obj.order_sn,
            # 我们商户自行生成的订单号
            out_trade_no=obj.order_sn,
            # 订单金额
            total_amount=obj.order_mount,
            # 成功付款后跳转到的页面，return_url同步的url
            return_url="http://47.105.128.181:8000/alipay/return/"
        )
        # 将生成的请求字符串拿到我们的url中进行拼接
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        return re_url

    class Meta:
        model = OrderInfo
        fields = "__all__"
    def create(self, validated_data):
        code = Random().randint(1, 5000)
        print(code)
        t=time.time()
        t=time.localtime(t)
        time_str = time.strftime("%Y%m%d%H%M%S",t)
        print(time_str)
        user_id = self.context['request'].user.id
        s = str(code) + str(time_str) + str(user_id)
        s=str(s)
        return OrderInfo.objects.create(user=validated_data['user'],
                                        post_script=validated_data['post_script'],
                                        order_mount=validated_data['order_mount'],
                                        signer_name=validated_data['signer_name'],
                                        singer_mobile=validated_data['singer_mobile'],
                                        order_sn=s)


class OrderGoodsSerializer(serializers.ModelSerializer):
    goods=GoodsSerializer(many=False)
    class Meta:
        model = OrderGoods
        fields = "__all__"
class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True)
    class Meta:
        model = OrderInfo
        fields = "__all__"
