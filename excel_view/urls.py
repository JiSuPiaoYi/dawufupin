from django.conf.urls import url,include
from excel_view import views


urlpatterns=[
    url(r'^index/', views.index,name='excel_view_index'),
    url(r'^create_dir/', views.create_dir,name='excel_create_dir'),#创建目录
    url(r'^guoban/', views.guoban, name='excel_guoban'),
    url(r'^file_view/', views.file_view, name='file_view'),#文件预览
    url(r'^file_del/', views.file_del, name='file_del'),#文件删除
    url(r'^upload_view/', views.upload_view, name='upload_view'),
    url(r'^upload_excel/', views.upload_excel, name='upload_excel'),
    url(r'^upload_excel_zc/', views.upload_excel_zc, name='upload_excel_zc'),
    url(r'^upload_excel_to/', views.upload_excel_to, name='upload_excel_to'),
    url(r'^create_index_excel_func/', views.create_index_excel_func, name='create_index_excel_func'),
    url(r'^search/', views.search, name='excel_search'),
    url(r'^sync_mysql/', views.SyncMysql.as_view(), name='sync_mysql'),#同步国办数据到数据库
    url(r'^data_correct/$', views.data_correct, name='data_correct'),#数据修正
    url(r'^data_correct_add/$', views.DataCorrectAdd.as_view(), name='data_correct_add'),#数据添加
    url(r'^data_correct_delete/$', views.data_correct_delete, name='data_correct_delete'),#数据删除
    url(r'^search_correct/$', views.SearchCorrect.as_view(), name='search_correct'),#数据修正-搜索
    url(r'^help_up/', views.HelpUp.as_view(), name='help_up'),  # 扶起来汇总
    url(r'^help_up_detail/$', views.HelpUpDetail.as_view(), name='help_up_detail'),  # 扶起来汇总详情
    url(r'^template_list/$', views.template_list, name='template_list'),  # 模板管理-列表
    url(r'^template_add/$', views.template_add, name='template_add'),  # 模板管理-添加
    url(r'^template_edit/$', views.template_edit, name='template_edit'),  # 模板管理-编辑
    url(r'^template_delete/$', views.template_delete, name='template_delete'),  # 模板管理-删除
    url(r'^template_download/$', views.template_download, name='template_download'),  # 模板管理-下载
    url(r'^excel_approve/$', views.excel_approve, name='excel_approve'),  # 审核
    url(r'^excel_approve1/$', views.excel_approve1, name='excel_approve1'),  # 审核-我提交的
    url(r'^approve_reject/$', views.approve_reject, name='approve_reject'),  # 审核-拒绝
    url(r'^approve_agree/$', views.approve_agree, name='approve_agree'),  # 审核-同意

    url(r'^ceshi/$', views.ceshi, name='ceshi'),
]