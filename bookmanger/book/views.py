from django.shortcuts import render

# Create your views here.
# 导入httpresponse模块
from django.http import HttpResponse


# 定义视图函数
def index(request):
    return HttpResponse('ok!')