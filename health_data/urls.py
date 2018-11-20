from django.conf.urls import url,include
from health_data import views


urlpatterns=[
    url(r'^four_one/$', views.four_one,name='four_one'),
]