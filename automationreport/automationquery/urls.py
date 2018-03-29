from django.conf.urls import url
from automationquery import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^index', views.index),
] + static(settings.STATIC_URL,docment_root = settings.STATIC_ROOT)
