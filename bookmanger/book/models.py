from django.db import models

# Create your models here.
# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    # 创建子字段,字段类型
    name = models.CharField(max_length=10)


# 准备人物列表信息的莫模型类
class PeopleTnfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束:人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)