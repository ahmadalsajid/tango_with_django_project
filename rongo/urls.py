from django.conf.urls import url
from rongo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
