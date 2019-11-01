"""django_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn_django.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^any$', index),
    url(r'^about$', about),
    url(r'^contact$', contact),
    url(r'^services$', services),
    url(r'^products$', products),
    url(r'^visitors$', visitors),
    url(r'^add_visitor$', add_visitor),
    url(r'^add_product$', add_product),
    url(r'^edit/(?P<id>\d+)', edit_product),
    
    # url(r'test$', dostuff),
    # url(r'^doanything', doanything)
]
