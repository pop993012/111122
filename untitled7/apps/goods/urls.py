from django.urls import path,include
from  apps.goods.views import GoodsView,GoodcateView,LBTcateView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'lst', GoodsView)
router.register(r'cate',GoodcateView)
router.register(r'banner',LBTcateView)

urlpatterns = [
  # path('lst/',GoodsView.as_view(),  name='goodsa'),
  # path('cate/',GoodcateView.as_view(),name='catea'),
  # path('banner/',LBTcateView.as_view(),name='banner')
  path('', include(router.urls))
  # path('',include(router.urls)
]
