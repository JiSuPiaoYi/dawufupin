from django.conf.urls import url,include
from user_center import views


urlpatterns=[
    url(r'^login_out/$', views.login_out,name='login_out'),
    url(r'^user_list/$', views.user_list,name='user_list'),
    url(r'^add_user/$', views.add_user,name='user_add'),
    url(r'^edit_user/$', views.edit_user,name='user_edit'),
    url(r'^delete_user/$', views.delete_user,name='user_delete'),
]