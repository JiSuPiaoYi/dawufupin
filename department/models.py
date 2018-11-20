from django.db import models
from django.contrib.auth.models import Group

# Create your models here.
class Department(models.Model):
    name = models.CharField('名称',max_length=100,default='')
    table_model = models.CharField('数据表模型',max_length=100,default='')
    pid = models.ForeignKey('self',verbose_name="上级部门",null=True,blank=True,on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, verbose_name="分组",null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门'