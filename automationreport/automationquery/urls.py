from django.conf.urls import url
from automationquery import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^index', views.index),
                  url(r'^login', views.login),
                  url(r'^cpu', views.cpu),
                  url(r'^launchapp', views.launchapp),
                  url(r'^menapp', views.menapp),
                  url(r'^interface', views.interface),
                  url(r'^functionapp', views.functionapp),
                  url(r'^functionweb', views.functionweb),
              ] + static(settings.STATIC_URL, docment_root=settings.STATIC_ROOT)
