"""devserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from api import views
from web import views as webviews
from app01 import views as app01views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', views.server_info),
    url(r'^server/', views.server.as_view()),
    url(r'^business/unit/list/', webviews.business_unit_list),
    url(r'^business/unit/add/', webviews.business_unit_add),
    url(r'^test/', app01views.test.as_view()),
    url(r'^courses/$', app01views.CourseView.as_view({"get":"list","post":"create"})),
    url(r'^courses/detail/$', app01views.CourseDetailView.as_view({"get": "list"})),
    url(r'^login/$', views.LoginView.as_view()),
]
