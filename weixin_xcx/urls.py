from django.conf.urls import url,include
from weixin_xcx import views


urlpatterns=[
    url(r'^is_account_bind/$', views.is_account_bind),
    url(r'^account_bind/$', views.account_bind),
    url(r'^relieve_bind/$', views.relieve_bind),
    url(r'^annunciate_list/$', views.annunciate_list),
    url(r'^annunciate_info/$', views.annunciate_info),
    url(r'^governmentdecree_list/$', views.governmentdecree_list),
    url(r'^governmentdecree_info/$', views.governmentdecree_info),
    url(r'^user_info/$', views.user_info),
    url(r'^change_password/$', views.change_password),
    url(r'^poorhouse_list/$', views.poorhouse_list),
    url(r'^poorhouse_detail/$', views.poorhouse_detail),
    url(r'^feedback/$', views.feedback)
]