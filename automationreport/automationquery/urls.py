# -*- coding: UTF-8 -*-
from django.conf.urls import url
from automationquery import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # 页面
                  url(r'^loginpage', views.loginpage),
                  url(r'^index', views.index),
                  url(r'^appQuery', views.appQuery),
                  url(r'^webFunctionQuery', views.webFunctionQuery),
                  url(r'^interfaceQuery', views.interfaceQuery),
                  url(r'^cpuQuery.html', views.cpuQuery),
                  url(r'^launchTime', views.launchTime),
                  url(r'^memoryQuery', views.memoryQuery),
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
                  url(r'^functioncount', views.functioncount),
                  url(r'^appfunctioncount', views.appfunctioncount),
                  url(r'^webfunctioncount', views.webfunctioncount),
                  url(r'^remoteip', views.get_remote_ip),
              ] + static(settings.STATIC_URL, docment_root=settings.STATIC_ROOT)
