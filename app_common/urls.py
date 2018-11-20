from django.conf.urls import url,include
from . import views


urlpatterns=[
    url(r'^nav/$', views.nav,name='nav_list'),
    url(r'^add_nav/$', views.add_nav,name='add_nav'),
    url(r'^edit_nav/$', views.edit_nav,name='edit_nav'),
    url(r'^del_nav/$', views.del_nav,name='del_nav'),
    url(r'^group_auth/$', views.group_auth,name='group_auth'),
    url(r'^upload_data/$', views.upload_data,name='upload_data'),
    url(r'^annunciate/$', views.Annunciate.as_view(),name='annunciate'),
    url(r'^annunciate_info/$', views.annunciate_info,name='annunciate_info'),
    url(r'^annunciate_delete/$', views.annunciate_delete,name='annunciate_delete'),
    url(r'^governmentdecree/$', views.GovernmentDecree.as_view(), name='governmentdecree'),
    url(r'^governmentdecree_info/$', views.governmentdecree_info, name='governmentdecree_info'),
    url(r'^governmentdecree_delete/$', views.governmentdecree_delete, name='governmentdecree_delete'),
    url(r'^log_list/$', views.log_list, name='log_list'),
    url(r'^log_detail/$', views.log_detail, name='log_detail'),
    url(r'^feedback_list/$', views.feedback_list, name='feedback_list'),
    url(r'^feedback_export/$', views.feedback_export),
    url(r'^affirm_feedback/$', views.affirm_feedback),
    url(r'^edit_remarks/$', views.edit_remarks),
    url(r'^sms_inform/$', views.sms_inform, name='sms_inform'),#短信通知
    url(r'^sms_inform_people/$', views.sms_inform_people, name='sms_inform_people'),  # 通知个人
    url(r'^sms_inform_department/$', views.sms_inform_department, name='sms_inform_department'),  # 通知部门
    url(r'^screen_common/$', views.screen_common, name='screen_common'),  # 大屏幕
    url(r'^screen/$', views.screen, name='screen'),  # 大屏幕
    url(r'^main1/$', views.main1, name='screen_main1'),  # 大屏幕
    url(r'^main2/$', views.main2, name='screen_main2'),  # 大屏幕
    url(r'^main3/$', views.main3, name='screen_main3'),  # 大屏幕
    url(r'^main4/$', views.main4, name='screen_main4'),  # 大屏幕
    url(r'^main5/$', views.main5, name='screen_main5'),  # 大屏幕
    url(r'^save_overcome_poverty/$', views.save_overcome_poverty, name='save_overcome_poverty'),  # 大屏幕
    url(r'^help_list/$', views.help_list, name='help_list'),  # 帮助中心
    url(r'^data_view/$', views.DataView.as_view()),

    url(r'^quchong/$', views.QuChong.as_view()),
    url(r'^ceshi/$', views.ceshi),
]