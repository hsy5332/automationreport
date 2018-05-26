# -*- coding: UTF-8 -*-
from django.conf.urls import url
from automationquery import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # 页面
                  url(r'^loginpage', views.loginpage),
                  url(r'^index', views.index),
                  url(r'^table', views.table),
                  # url(r'^chart', views.chart),
                  # url(r'^empty', views.empty),
                  # url(r'^form', views.form),
                  # url(r'^tabpanel', views.tabpanel),
                  # url(r'^uielements', views.uielements),
                  # 接口
                  url(r'^login', views.login),
                  url(r'^cpu', views.cpu),
                  url(r'^launchapp', views.launchapp),
                  url(r'^menapp', views.menapp),
                  url(r'^interface', views.interface),
                  url(r'^functionapp', views.functionapp),
                  url(r'^functionweb', views.functionweb),
              ] + static(settings.STATIC_URL, docment_root=settings.STATIC_ROOT)
