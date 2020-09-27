from django.urls import path
from book3.views import index, register,register1,register2, goods,get,post,shop
from book3.views import json,json1,json2,response,response1,response3,LoginView
from book3.views import goods1,get1,get2,set_cookie,get_cookie,get_session,set_session
from book3.views import OrderView,middleware
from django.urls import converters
from django.urls.converters import register_converter
# # 1.定义转换器
class MobileConverter:
    # 验证数据的关键是： 正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据，给视图函数
    def to_python(self, value):
        return value

register_converter(MobileConverter,'phone')

urlpatterns = [
 path('index/', index),
 # path('<int:city_id>/<phone:mobile>', shop),
 path('register/', register),
 path('register1/', register1),
 path('register2/', register2),
 path('json/', json),
 path('json1/', json1),
 path('json2/', json2),
 # path('<city_id>/<good_id>/', goods),
 # path('<city_id1>/<good_id1>/', goods1),
 path('get/', get),
 path('get1/', get1),
 path('get2/', get2),
 path('post/', post),
 path('response/', response),
 path('response1/', response1),
 path('response3/', response3),
 path('set_cookie/', set_cookie),
 path('get_cookie/', get_cookie),
 path('set_session/', set_session),
 path('get_session/', get_session),
 path('login/', LoginView.as_view()),
 path('order/', OrderView.as_view()),
 path('middleware/',middleware)



 # path('cookie/',cookie)
]