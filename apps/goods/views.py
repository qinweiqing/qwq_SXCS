# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.views import APIView
# from goods.serializers import GoodsSerialzers
# from .models import Goods
# from rest_framework.response import Response
# # Create your views here.
#
# class GoodsList(APIView):
#     '''
#     商品列表
#     '''
#     def get(self,request,format=None):
#         goods=Goods.objects.all()
#         goods_serialzer=GoodsSerialzers(goods,many=True)
#         return Response(data=goods_serialzer.data,status=status.HTTP_200_OK)

from rest_framework import filters
from goods.serializers import GoodsSerialzers,GoodsCategory,CategorySerializer
from .models import Goods
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
# from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend




# class GoodsList(mixins.ListModelMixin,generics.GenericAPIView):
#     # 商品列表页
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerialzers
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

class GoodsPagination(PageNumberPagination):
#     商品列表自定义分页
#     默认每页显示的个数
    page_size = 12
#     可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
#       页码参数
    page_query_param = 'page'
#       最多能显示多少页
    max_page_size = 100

# class GoodsList(generics.ListAPIView):
#     # 商品列表页
#     queryset = Goods.objects.all()
#     pagination_class = GoodsPagination
#     serializer_class = GoodsSerialzers

class GoodsListSet(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    # 商品列表页
    # 这里必须要定义一个默认的排序,否则报错
    queryset = Goods.objects.all().order_by('id')
    pagination_class = GoodsPagination
    serializer_class = GoodsSerialzers
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)


    # 设置filter的类为我们自定义的类
    filter_class=GoodsFilter

#     搜索，=name表示精确搜索，也可以使用各种正则表达式
    search_fields=('=name','goods_brief','goods_desc')

#       排序
    ordering_fields=('sold_num','shop_price')



class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''list:商品分类列表数据'''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer