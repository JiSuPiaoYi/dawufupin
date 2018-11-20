from django.db import models
from django.contrib.auth.models import User
from department.models import Department

# Create your models here.

class UserExtra(models.Model):   #用户表
    mobile = models.CharField('联系电话', max_length=15, primary_key=True)
    name = models.CharField('姓名', blank=True,default='', max_length=100)
    about = models.ForeignKey(User, db_column='user_id',on_delete=models.CASCADE)
    openid = models.CharField(blank=True, default='', max_length=50)
    token = models.CharField(blank=True, default='', max_length=32)
    department = models.ForeignKey(Department,verbose_name="所属部门",null=True,blank=True,on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '账号'