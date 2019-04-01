from django.urls import path,re_path,include
from .views import GoodFarViewA, UserAdderessView

from rest_framework.routers import  DefaultRouter

router = DefaultRouter()
router.register(r'fav',GoodFarViewA)
router.register(r'address', UserAdderessView)

urlpatterns = [
    path('', include(router.urls)),
]
