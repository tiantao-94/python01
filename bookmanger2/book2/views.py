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

# *************************************
# 查询操作
# 单条信息查询用get
try:
    book=BookInfo.objects.get(id=5)
except Exception as e:
    pass
    print('查询结果不存在')
# 多条信息查询用all
BookInfo.objects.all()
from book2.models import PeopleInfo
PeopleInfo.objects.all()


# count 查询结果的数量
BookInfo.objects.all().count()
BookInfo.objects.count()

# ***************过滤查询*************
# filter 过滤出多个结果      模型类名.objects.filter(属性名__运算符=值)
# exclude 排除符合条件剩余的结果  模型类名.objects.exclude(属性名__运算符=值)
# get过滤单个结果        模型类名.objects.get(属性名__运算符__运算符=值)
# 查询编号为1的图书
book=BookInfo.objects.get(id=1)   #简写方式
book=BookInfo.objects.get(id__exact=1)  #完整写法
BookInfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])

#*************** 比较查询*****************
# 查询编号大于3的图
# 大于 gt             great 大
# 大于等于 gte        e  equal
#
# 小于 lt             litte
# 小于等于 lte
BookInfo.objects.filter(id__gt=3)
# 查询编号不等于3的书籍
BookInfo.objects.exclude(id=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1980-1-1')


# F对象和Q对象查询
# 导入对象Q  F
from django.db.models import F
# 语法查询格式  filter使用  模型类名.objects.fliter(属性名__运算符=F('第二个属性)
# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# 并且查询
# 查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
BookInfo.objects.filter(readcount__gt=20,id__lt=3)

from django.db.models import Q
# 或者语法：  模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|...)
# 并且语法：  模型类名.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&...)
# not 非 语法：  模型类名.objects.filter(～Q(属性名__运算符=值))

# 查询阅读量大于20，或者编号小于3的图书。
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
# 查询编号不等于3的书籍
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))


#******************聚合函数*********************
from django.db.models import Sum,Max,Min,Avg,Count
# 语法格式   模型类名.objects.aggregate(xxx('字段名')
BookInfo.objects.aggregate(Sum('readcount'))

#**********************排序********************
BookInfo.objects.all().order_by('readcount')


# 两张表的级联操作
# 查询书籍为1的所有人物信息
book1=BookInfo.objects.get(id=1)
print(book1)

# 获取了id为1的书籍
BookInfo.objects.filter(id=1)
# 主表查询副表属性查询
book2=BookInfo.objects.get(id=1)
book2.peopleinfo_set.all()
# 副表查询主表
# 查询人物为1的书籍信息
person = PeopleInfo.objects.get(id=1)
person.book.name
person.book.readcount


###############关联过滤查询#####################
# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name='郭靖')
# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')
# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')
# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)