from django.conf.urls import url,include
from . import views


urlpatterns=[
    url(r'^index/$', views.index,name='department_index'),
    url(r'^add/$', views.add,name='department_add'),
    url(r'^edit/$', views.edit,name='department_edit'),
    url(r'^del/$', views.delete,name='department_delete')
]