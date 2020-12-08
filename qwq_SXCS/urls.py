"""qwq_SXCS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.views.static import serve

from django.contrib import admin
from django.urls import path,include,re_path
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from qwq_SXCS.settings import MEDIA_ROOT
from goods.view_base import GoodsDetail
from goods.views import GoodsListSet,CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from users.views import SmsCodeViewset,UserViewset
from user_operation.views import UserFavViewset,LeavingMessageViewset,AddressViewset
from trade.views import ShoppingCartViewset,OrderViewset
router=DefaultRouter()
# 配置购物车url
router.register(r'shopcarts',ShoppingCartViewset,basename='shopcarts')
router.register(r'orders',OrderViewset,basename='orders')
# 配置用户收藏的url
router.register(r'userfavs',UserFavViewset,basename='userfavs')
router.register(r'messages',LeavingMessageViewset,basename='messages')
router.register(r'address',AddressViewset,basename='address')
# 配置users的url
router.register(r'users',UserViewset,basename='users')
# 配置codes的url
router.register(r'code',SmsCodeViewset,basename='code')
# 配置goods的url
router.register(r'goods',GoodsListSet)
router.register(r'categorys',CategoryViewSet,basename="categorys")
urlpatterns = [
    re_path('^',include(router.urls)),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),
    path('media/<path:path>',serve,{"document_root":MEDIA_ROOT}),
    # path('good_detail/',GoodsDetail.as_view(),name='good_detail'),
    path('good_list/',GoodsListSet.as_view({'get':'list'}),name='good_list'),
#     drf文档，title自定义
    path('docs',include_docs_urls(title="葵花宝典")),
    path('api-auth/',include('rest_framework.urls')),

#     token
    path('api-token-auth/',views.obtain_auth_token),

    path('jwt-auth/',obtain_jwt_token),

#     jwt的认证接口
    path('login/',obtain_jwt_token),


]
