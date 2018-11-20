from django.db import models

# Create your models here.

#excel审批
class ExcelApprove(models.Model):
    create_time = models.DateTimeField(verbose_name="上传时间",auto_now_add=True,null=True)
    approve_time = models.DateTimeField(verbose_name="审批时间", null=True)
    upload_user_id = models.IntegerField(blank=True,null=True)#上传人
    user_id = models.IntegerField(blank=True,null=True)#审批人
    remark = models.TextField('备注',blank=True,null=True)
    path = models.CharField('文件路径',max_length=500,blank=True,null=True)
    department_id = models.IntegerField(blank=True,null=True)#部门id
    status = models.SmallIntegerField('状态',default=2)#0拒绝，1同意，2未审批

    class Meta:
        verbose_name = 'excel审批'

class Template(models.Model):
    title = models.CharField('标题', max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name="上传时间",auto_now_add=True,null=True)
    user_id = models.IntegerField(blank=True,null=True)#创建人
    row = models.TextField('列字段',blank=True,null=True)
    remark = models.TextField('备注',blank=True,null=True)
    policy_object = models.CharField(max_length=10, db_column='policy_object', blank=True,default='')  # 政策针对对象（村/户/人）

    class Meta:
        verbose_name = '模板管理'