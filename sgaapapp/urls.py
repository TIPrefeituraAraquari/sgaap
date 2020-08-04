# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import url

from .views.home import HomeView

urlpatterns = [
    # url(r'/home', HomeView.as_view(),name='home'),
    url(r'', HomeView.as_view(),name='home'),

]