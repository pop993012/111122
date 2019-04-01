from django.shortcuts import render
from django.views import View
# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from  .models import Goods,GoodsCategory,BannerLBT
from  .serializer import GoodsSerializer,CategarySerializer,LbtSerialier
from django.http import JsonResponse
from rest_framework import filters as resfilters
from rest_framework.views import APIView
# class GoodsView(View):
#     def get(self,request):
#         pros=Goods.objects.all()
#         pros=GoodsSerializer(pros,many=True)
#         return JsonResponse(pros.data,safe=False)


# class GoodsView(APIView):
#     '''
#      print(1111)
#     '''
#     def get(self,request):
#         pros = Goods.objects.all()
#         pros = GoodsSerializer(pros, many=True)
#         return Response(pros.data)


# from rest_framework import mixins
# from rest_framework import generics
# class GoodsView(mixins.ListModelMixin,
#                   generics.GenericAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     def get(self, request, *args, **kwargs):
#             return self.list(request, *args, **kwargs)
#     def get_queryset(self): # 过滤
#             key = self.request.query_params['name'] # 查询的参数
#             return Goods.objects.filter(name__contains=key)
from rest_framework import generics
import django_filters
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated,AllowAny

class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100



class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="market_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="market_price", lookup_expr='lte')
    name = filters.CharFilter(field_name='name',lookup_expr='contains')
    category =filters.NumberFilter(field_name='category',method='filterGoodsByCategary')

    def filterGoodsByCategary(self, queryset, name, value):
        print(value)
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price','name','category']


class GoodsView(viewsets.ReadOnlyModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,resfilters.SearchFilter,resfilters.OrderingFilter)
    filterset_class = ProductFilter

    ordering_fields = ('sold_num', 'shop_price')
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # permission_classes = (AllowAny,)

class GoodcateView(viewsets.ReadOnlyModelViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1).all()
    serializer_class = CategarySerializer
    # permission_classes = (AllowAny,)


class LBTcateView(viewsets.ReadOnlyModelViewSet):
    queryset = BannerLBT.objects.filter(active=True).all()
    serializer_class = LbtSerialier