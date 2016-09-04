from django.conf.urls import url
from django.views.generic import ListView, DetailView

from voterx_app import views
from voterx_app import models

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^name/$', views.NameView.as_view()),
    url(r'^post/$', views.PostView.as_view()),
]