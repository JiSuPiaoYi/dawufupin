from django.db import models
from django.contrib.auth.models import Permission

# Create your models here.
class Nav(models.Model):
    name = models.CharField('名称',max_length=100,default='')
    is_show = models.BooleanField('是否显示',default=True,blank=True)
    url = models.URLField('url',default='#')
    pid = models.ForeignKey('self',verbose_name="上级导航",null=True,blank=True,limit_choices_to={'pid__in': [0]},on_delete=models.CASCADE)
    icon = models.CharField('图标',max_length=100,default='',blank=True)
    sort = models.SmallIntegerField('排序',default='1')
    permission = models.ForeignKey(Permission,verbose_name="权限",null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '导航'
        verbose_name_plural = '导航'

#通告
class Annunciate(models.Model):
    title = models.CharField('标题',max_length=100,default='')
    content = models.TextField('内容',default='')
    attach_path = models.CharField('附件路径',max_length=100)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
        verbose_name = '通告'

#政令
class GovernmentDecree(models.Model):
    title = models.CharField('标题',max_length=100,default='')
    content = models.TextField('内容',default='')
    attach_path = models.CharField('附件路径', max_length=100)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
        verbose_name = '政令'

#日志
class Logs(models.Model):
    action_time = models.DateTimeField(verbose_name="操作时间",auto_now_add=True,null=True)
    user_id = models.IntegerField()
    message = models.CharField('简介',max_length=500,blank=True,null=True)
    detail = models.TextField('详细',blank=True,null=True)

    class Meta:
        verbose_name = '日志'

#意见反馈
class Feedbacks(models.Model):
    TYPE_CHOOSE = (
        (1,'建议'),
        (2,'贫困户基本信息数据问题'),
        (3,'贫困户享受政策数据问题'),
        (4,'其他问题')
    )
    create_time = models.DateTimeField(verbose_name="反馈时间",auto_now_add=True,null=True)
    user_id = models.IntegerField()
    type = models.CharField('类型',max_length=500,blank=True,null=True)
    content = models.TextField('内容',blank=True,null=True)
    img_path = models.CharField('图片路径',max_length=500,blank=True,null=True)
    about_object_type = models.SmallIntegerField('涉及对象类型', default=0)  # 1贫困人口，2贫困户
    about_object = models.CharField(max_length=500,blank=True,null=True)
    about_object_content = models.CharField(max_length=500,blank=True,null=True)
    status = models.SmallIntegerField('状态', default=2)  # 1确定，2未确定
    remarks = models.CharField(max_length=300,default='', blank=True)  # 备注

    class Meta:
        verbose_name = '意见反馈'

#帮助
class HelpCenter(models.Model):
    title = models.CharField('标题', max_length=500, blank=True, null=True)
    content = models.TextField('内容',blank=True,null=True)

    class Meta:
        verbose_name = '帮助'

