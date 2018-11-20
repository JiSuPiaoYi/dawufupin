"""dawufupin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from user_center.views import login_in
from app_common.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index,name='index'),
    url(r'^login_in/$', login_in,name='login_in'),
    url(r'^app_common/',include('app_common.urls')),
    url(r'^user_center/',include('user_center.urls')),
    url(r'^department/',include('department.urls')),
    url(r'^report_form/',include('report_form.urls')),
    url(r'^excel_view/',include('excel_view.urls')),
    url(r'^health_data/',include('health_data.urls')),

    url(r'^weixin_xcx/',include('weixin_xcx.urls'))
]