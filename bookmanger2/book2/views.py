from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book2.models import BookInfo


def index(request):
    # 在这里实现增删改查
    # 获取书籍信息表所有内容
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse('index')


# 增加数据方式1
from book2.models import BookInfo

book = BookInfo(
    name='Django',
    pub_date='2020-11-11',
    readcount=10

)
# 需要手动调用  对象的save方法才能保存导数据中
book.save()

# 方法2
# objects 相当于一个代理 实现增删改查
BookInfo.objects.create(
    name='测试数据',
    pub_date='2008-8-8',
    readcount='33'
)

# 修改数据
# 方法1
# 先找到要修改的数据在进行修改
book = BookInfo.objects.get(id=6)
book.name = '运维测试'
# 想要保存数据 需要调用对像的save方法
book.save()

# 方法2 使用filter过滤
BookInfo.objects.filter(id=6).update(name='爬虫数据',readcount=666)

# 删除数据
# 方法1
book = BookInfo.objects.get(id=6)
book.delete()

# 方法2
BookInfo.objects.get(id=5).delete()

