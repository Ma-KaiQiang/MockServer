"""MockServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from mdc_mock.views import *
from authorization import views
from django.urls import re_path as url

urlpatterns = [
    path('mock/', include('mdc_mock.urls')),
    path('index/', views.index),
    path('login/', views.login),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register),
    path('test/', views.test),
    # re_path('^.*', MdcMockResponseView.as_view())
]
