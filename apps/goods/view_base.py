# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import GoodsSerialzers
# from .models import Goods
#
# class GoodsDetail(APIView):
#     def get(self,request):
#         good=Goods.objects.all()
#         good_=GoodsSerialzers(instance=good,many=True)
#         # print(good_)
#         return Response(data=good_.data,status=status.HTTP_200_OK)


from django.views.generic import View
from goods.models import Goods
from django.http import JsonResponse,HttpResponse
import json
from django.core import serializers
class GoodsDetail(View):
    def get(self,request):
        json_list=[]
        goods=Goods.objects.all()
        # 一个一个字段提取的麻烦，就用model_to_dict，将整个model转化成dict
        # for good in goods:
        #     json_dict={}
        #     json_dict["name"]=good.name
        #     print("json_dict['name']=",json_dict['name'])
        #     json_dict["category"]=good.category.name
        #     json_dict["market_price"]=good.market_price
        #     json_list.append(json_dict)
        #     print("json_list",json_list)



        # 此方法使用会出现ImageField不可序列化
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict=model_to_dict(good)
        #     print("json_dict=",json_dict)
        #     json_list.append(json_dict)

        # 就要用到django的serializers
        # json_data=serializers.serialize('json',goods)
        # print("json_data=",json_data)
        # json_data=json.loads(json_data)
        # print("json_data=",json_data)

        # return JsonResponse(json_data,safe=False)

