from django.db import models
# 数据库操作命令大全

# shell命令行开启（进入shell环境）
# python manage.py shell
# 提示nameXXX is not defined，是没有声明，加入申明
# from shop.models import Person

# 数据库更新命令(不进入shell环境调用)
# python manage.py makemigrations
# python manage.py migrate

# 数据库增加命令（新建时返回的是True, 已经存在时返回False）（shell环境内）
# Person.objects.get_or_create(name="WZT", age=23)

# Create your models here.

# 数据库按照某个名字删除命令（新建时返回的是True, 已经存在时返回False）
# Person.objects.filter(name__contains="1111WZT").delete() # 删除 名称中包含 "abc"的人
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class UserId(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name

def addPserson():
    i=1
    sum=10055
    while(i<sum):
        Person.objects.get_or_create(name="username"+str(i), age=i)
        i=i+1

