from .models import Goods, GoodsCategory, GoodsImage
from rest_framework import serializers


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GoodsCategory
#         fields = "__all__"


# class GoodsSerialzers(serializers.Serializer):
#
#         click_num=serializers.IntegerField(default=0)
#         name=serializers.CharField(required=True,max_length=100)
#         goods_front_image=serializers.ImageField()

class CategorySerializer3(serializers.ModelSerializer):
    '''三级分类'''
    class Meta:
        model=GoodsCategory
        fields='__all__'

class CategorySerializer2(serializers.ModelSerializer):
    '''二级分类'''
    # 在parent_category字段中定义的related_name="sub_cat"
    sub_cat=CategorySerializer3(many=True)
    class Meta:
        model=GoodsCategory
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    '''商品一级类别序列化'''
    sub_cat=CategorySerializer2(many=True)
    class Meta:
        model=GoodsCategory
        fields="__all__"

class GoodsSerialzers(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Goods
        fields='__all__'


# # 轮播图
# class GoodsImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=GoodsImage
#         fields=('image',)
#
# # 商品列表页
# class GoodsSerializer(serializers.ModelSerializer):
#     # 覆盖外键字段
#     category=CategorySerializer()
# #     images是数据库中设置related_name='images'，把轮播图嵌套进来
#     images=GoodsImageSerializer(many=True)
#     class Meta:
#         model=Goods
#         fields='__all__'
