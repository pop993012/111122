from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import  GoodsFar,UserAddress
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializer import  GoodsFarSer,UserGoodsFarSer,UserAddresserializers
# Create your views here.

class  GoodFarViewA(viewsets.ModelViewSet):
    queryset = GoodsFar.objects.all()
    def get_serializer_class(self):
        if self.action  == 'list': # 查找全部
            return UserGoodsFarSer
        return GoodsFarSer
    def get_queryset(self):
        return GoodsFar.objects.filter(user=self.request.user)
    permission_classes = (IsAuthenticated,)
    authentication_classes = [BasicAuthentication, JSONWebTokenAuthentication,]
    lookup_field = 'goods_id'




class  UserAdderessView( viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    permission_classes = (IsAuthenticated,)  # 必须是自己
    serializer_class = UserAddresserializers
    authentication_classes = [BasicAuthentication, JSONWebTokenAuthentication]
    def get_queryset(self):
        return   UserAddress.objects.filter(user=self.request.user)