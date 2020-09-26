from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from book3.models import BookInfo


def index(request):
    book= BookInfo.objects.create(
        name='张飞',
        pub_date='2020-3-5',
        readcount=888
    )

    return HttpResponse('index')


# 请求体 form  表单发送请求
def register(request):
    data = request.POST
    print(data)
    return HttpResponse('register')

def register1(request):
    data= request.POST
    print(data)
    return HttpResponse('hello register1')

def register2(request):
    data=request.POST
    print(data)
    username=data.body
    # return HttpResponse('hello register2')
    return JsonResponse


# 请求体 raw 发送请求
def json(request):
    # json数据不能通过request,post接收数据
    body = request.body
    # print(body)
    body_str=body.decode()
    # print(body_str)
    # josn形式的字符串 可以转换成python字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    return HttpResponse('json')

def json1(request):
    # json不能通过request.post来接收数据
    body = request.body
    # 获取json类型的字符串
    body_str=body.decode()
    # 转换成python中的字符串类型
    import json
    body_dric=json.loads(body_str)
    print(body_dric)
    return HttpResponse('hello json1')

def json2(request):
    body=request.body
    # 获取字符串类型
    body_str=body.decode()
    # 转换为python字符串 导入json包
    import json
    body_dict=json.loads(body_str)
    print(body_dict)
    return HttpResponse('hello json2')


# url路径方式请求
def goods(request, city_id, good_id):
    print(city_id,good_id)
    return JsonResponse({'city_id':city_id,'good_id':good_id})
    # return HttpResponse('city_id:city_id,good_id:good_id')


def goods1(request,city_id1,good_id1):
    print(city_id1,good_id1)
    return JsonResponse({'city_id1':city_id1,'good_id1':good_id1})


# def goods(request,city_id,good_id):
#     return JsonResponse({'city_id':city_id,'good_id':good_id})

# 获取请求路径中的查询字符串参数
def get(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    print(a)
    print(b)
    return HttpResponse('hello get')


def get1(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    print(a, b)
    return HttpResponse('hello get1')


def get2(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    print(a, b)
    return HttpResponse('hello get2')


# 请求体发送数据
def post(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.get('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('hello post')


#转换器版本提取路径传参
def shop(request,city_id,mobile):
    print(city_id,mobile)
    #获取请求信息
    query_params=request.GET
    print(query_params)
    order = query_params.getlist('order')
    return HttpResponse('我的商店')

#response对象
def response(request):
    info = {
        'name': 'itcast',
        'address': 'shunyi'}
    response=JsonResponse(info,status=300)
    response['name']='xiaoming'
    return response

def response1(request):
    girl_firends = [
        {
            'name': 'rose',
            'address': 'shunyi'
        },
        {
            'name': 'jack',
            'address': 'changping'
        }
    ]
    #girl_firends是列表,我们返回的数据一般是字典类型
    # JsonResponse 可以把字典转换为json
    #现在给了一个非字典数据， 出了问题我们自己负责 safe=FALSE
    response=JsonResponse(girl_firends, safe=False)
    return response

def response3(request):
    response=HttpResponse('res',status=200)
    #响应头
    response['name']='tiaoyao'
    return response