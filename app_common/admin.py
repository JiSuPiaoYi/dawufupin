from django.contrib import admin
from app_common.models import HelpCenter

# Register your models here.
@admin.register(HelpCenter)
class HelpCenterAdmin(admin.ModelAdmin):
    list_display = ('title',)

    search_fields = ['title']  # 搜索字段

    class Media:
        css ={
            "all": ("/common/css/flatpage.css",)
        }
        js = (
            '/common/source/jquery/jquery-3.1.1.min.js',
            '/common/source/wangEditor/wangEditor.min.js',
            '/common/js/flatpage_wangEditor.js'
        )