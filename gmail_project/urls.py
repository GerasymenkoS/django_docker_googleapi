"""gmail_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from gmail_project import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^admin/', admin.site.urls),
    url(r'logout/$', views.logout_),
    url(r'index/$', views.index),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'oauth2callback/$', views.auth_return),
    url(r'get_emails/$', views.get_all_emails)
]

