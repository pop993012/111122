"""untitled7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include,re_path
import xadmin
from django.views.static import serve
from untitled7.settings import MEDIA_ROOT
from rest_framework_jwt.views import obtain_jwt_token
from apps.trade.views import ShopCarView,OrderInfoView,OrderGoodsView,AlipayView
from rest_framework.authtoken import views as aa
from rest_framework.routers import  DefaultRouter
router = DefaultRouter()
router.register(r'shopcarts',ShopCarView)
router.register(r'orderinfo',OrderInfoView)
router.register(r'ordergoods',OrderGoodsView)
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.cache import cache
import requests
def index(request):
    s=render_to_string('index.html')
    return render(request,'index.html')





urlpatterns = [
 path('goods/',include('apps.goods.urls')),
 re_path(r'^api-auth/', include('rest_framework.urls')),
 path('xadmin/', xadmin.site.urls),
path('ueditor/',include('DjangoUeditor.urls' )),
path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
path('jwt-auth/', obtain_jwt_token ),
 path('fav/',include('apps.user_operation.urls')),
 path('',include(router.urls)),
# path(r'^api/', include('backend.urls', namespace='api')),
path(r'api-token-auth/',aa.obtain_auth_token),

 path('a/',index),
 path('alipay/return/', AlipayView.as_view(),name='aaaaaaa'),
path('', include('social_django.urls', namespace='social'))
]
