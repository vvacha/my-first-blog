# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
import os.path


from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]