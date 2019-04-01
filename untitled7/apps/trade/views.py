from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import ShopCar, OrderInfo, OrderGoods
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializer import ShopCarSerializers, PostShopCarSerializers
from apps.goods.models import Goods
from .serializer import OrderInfoSerializer, OrderGoodsSerializer, OrderDetailSerializer
from django.views.decorators.csrf import csrf_exempt, csrf_protect


class ShopCarView(viewsets.ModelViewSet):
    queryset = ShopCar.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return ShopCarSerializers
        return PostShopCarSerializers

    authentication_classes = [BasicAuthentication, JSONWebTokenAuthentication]

    def get_queryset(self):
        return ShopCar.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(999955441)
        user = self.request.user
        goods = serializer.data['goods']
        shop = ShopCar.objects.filter(user=user, goods_id=goods).first()
        gs = Goods.objects.filter(id=goods).first()
        gs.goods_num -= serializer.data['nums']
        gs.save()
        if shop:
            shop.nums += serializer.data['nums']
            shop.save()
        else:
            ShopCar.objects.create(goods_id=goods, nums=serializer.data['nums'], user=user)

    def perform_update(self, serializer):
        print(8)
        # car_id=serializer.data['id']
        goos_id = serializer.data['goods']
        print(goos_id)
        shopgoods = ShopCar.objects.filter(user=self.request.user, goods_id=goos_id).first()
        print('OK')
        print(shopgoods.nums)
        print(serializer.initial_data['nums'])
        print(shopgoods.goods)
        goods = Goods.objects.filter(id=goos_id).first()
        max = shopgoods.nums - serializer.initial_data['nums']
        print(max)
        print(serializer.data['nums'])
        shopgoods.nums = serializer.initial_data['nums']
        shopgoods.save()
        goods.goods_num += max
        goods.save()

    def perform_destroy(self, instance):
        goods = instance.goods
        shopcar = ShopCar.objects.filter(pk=instance.pk).first()
        goods.goods_num += shopcar.nums
        shopcar.delete()
        goods.save()


class OrderInfoView(viewsets.ModelViewSet):
    queryset = OrderInfo.objects.all()
    permission_classes = (IsAuthenticated,)  # 必须是自己
    authentication_classes = [BasicAuthentication, JSONWebTokenAuthentication]
    serializer_class = OrderInfoSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderInfoSerializer

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order = serializer.save()
        shops = ShopCar.objects.filter(user=self.request.user).all()
        for shop in shops:
            OrderGoods.objects.create(
                order=order,
                goods=shop.goods,
                nums=shop.nums
            )
            shop.delete()


class OrderGoodsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  # 必须是自己
    authentication_classes = [BasicAuthentication, JSONWebTokenAuthentication]
    queryset = OrderGoods.objects.all()

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)

    serializer_class = OrderGoodsSerializer


# from untitled7 import settings
# from alipay import AliPay
# import os
# ali_pay=AliPay(
#       appid=settings.ALIPAY_APPID,
#       app_notify_url = None,
#       app_private_key_path = os.path.join(settings.BASE_DIR, 'keys/a'),
# alipay_public_key_path = os.path.join(settings.BASE_DIR, 'keys/pub'),
# debug = False,
#   )
from rest_framework.views import APIView
from .util.aliPay import AliPay
from datetime import datetime
from rest_framework.response import Response
from django.shortcuts import HttpResponseRedirect


class AlipayView(APIView):
    def get(self, request):
        processed_dict = {}
        # 取出post里面的数据
        for key, value in request.GET.items():
            processed_dict[key] = value
        # 把signpop掉，文档有说明
        sign = processed_dict.pop("sign", None)

        # 生成一个Alipay对象
        alipay = AliPay(
            appid="2016092000553304",
            app_notify_url="http://47.105.111.148:8000/alipay/return/",
            app_private_key_path='apps/trade/keys/a.txt',
            alipay_public_key_path='apps/trade/keys/zfb.txt',  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://47.105.111.148:8000/alipay/return/"
        )

        # 进行验证
        verify_re = alipay.verify(processed_dict, sign)

        # 如果验签成功
        if verify_re is True:
            # 商户网站唯一订单号
            order_sn = processed_dict.get('out_trade_no', None)
            # 支付宝系统交易流水号
            trade_no = processed_dict.get('trade_no', None)
            # 交易状态
            trade_status = processed_dict.get('trade_status',True)

            # 查询数据库中订单记录(根据订单号查询订单)
            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)

            for existed_order in existed_orders:
                # 订单商品项
                order_goods = existed_order.goods.all()  # 订单的详情
                # 商品销量增加订单中数值
                for order_good in order_goods:
                    goods = order_good.goods  # 获取到所有的商品
                    goods.sold_num += order_good.goods_num  # 销量进行累加
                    goods.save()  # 保存到数据库中

                # 更新订单状态
                existed_order.pay_status = trade_status  # 修改订单的状态
                existed_order.trade_no = trade_no  # 支付宝的流水号
                existed_order.pay_time = datetime.now()  # 支付时间
                existed_order.save()  # 更新订单信息
            # 需要返回一个'success'给支付宝，如果不返回，支付宝会一直发送订单支付成功的消息
            return HttpResponseRedirect('http://47.105.128.181:8000/aa/')
        else:
            return Response('支付失败,sign不成功')

    def post(self, request):
        pass
        """
        处理支付宝的notify_url (必须是公网ip才行)
        """
        # 存放post里面所有的数据
        processed_dict = {}
        # 取出post里面的数据
        for key, value in request.POST.items():
            processed_dict[key] = value
        # 把signpop掉，文档有说明
        sign = processed_dict.pop("sign", None)

        # 生成一个Alipay对象
        alipay = AliPay(
            appid="2016092000553304",
            app_notify_url="http://47.105.111.148:8000/alipay/return/",
            app_private_key_path='apps/trade/keys/a.txt',
            alipay_public_key_path='apps/trade/keys/zfb.txt',  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://47.105.111.148:8000/alipay/return/"
        )

        # 进行验证
        verify_re = alipay.verify(processed_dict, sign)

        # 如果验签成功
        if verify_re is True:
            # 商户网站唯一订单号
            order_sn = processed_dict.get('out_trade_no', None)
            # 支付宝系统交易流水号
            trade_no = processed_dict.get('trade_no', None)
            # 交易状态
            trade_status = processed_dict.get('trade_status', None)

            # 查询数据库中订单记录
            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                # 订单商品项
                order_goods = existed_order.goods.all()
                # 商品销量增加订单中数值
                for order_good in order_goods:
                    goods = order_good.goods
                    goods.sold_num += order_good.goods_num
                    goods.save()

                # 更新订单状态
                existed_order.pay_status = trade_status
                existed_order.trade_no = trade_no
                existed_order.pay_time = datetime.now()
                existed_order.save()
            # 需要返回一个'success'给支付宝，如果不返回，支付宝会一直发送订单支付成功的消息
            return Response("success")
