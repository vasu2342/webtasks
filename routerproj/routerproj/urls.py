"""routerproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
import ipaddress 
# from rest_framework.authtoken import *
from routerapp import views
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    # url(r'',views.apicall),
    path('admin/', admin.site.urls),
    path('create/', views.RouterCreateAPIView.as_view(),name='create'),
    path('list/', views.RouterAPIView.as_view()),
    path('retrieve/<str:sapid>', views.RouterDetailAPIView.as_view()),
    path('delete/<str:loopbackipv4>', views.RouterDeleteAPIView.as_view()),
    path('update/<str:loopbackipv4>', views.RouterUpdateAPIView.as_view()),
    path('get-api-token/', auth_view.obtain_auth_token,name='get-api-token'),
]
# 