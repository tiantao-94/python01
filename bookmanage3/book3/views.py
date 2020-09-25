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
    return HttpResponse('hello register2')


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


# url路径方式请求
def goods(request, city_id, good_id):
    return JsonResponse({'city_id':city_id,'good_id':good_id})


# 获取请求路径中的查询字符串参数
def get(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    print(a)
    print(b)
    return HttpResponse('hello get')


# 请求体发送数据
def post(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.get('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('hello post')
