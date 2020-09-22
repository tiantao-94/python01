from django.shortcuts import render

# Create your views here.
# 导入httpresponse模块
# from django.http import HttpResponse
# 导入render模板
from django.shortcuts import render


# 定义视图函数
def index(request):
    #准备上下文:定义在字典中的数据
    context = {'title':'欢迎来到德莱联盟'}
    # return HttpResponse('ok!')
    return render(request, 'book/index.html', context)