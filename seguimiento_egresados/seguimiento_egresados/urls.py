"""seguimiento_egresados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import CustomLoginView
from seguimiento_egresados import settings

urlpatterns = [
    path('%sadmin/' % settings.PATH_PREFIX, admin.site.urls, name='admin'),
    path('', include(('accounts.urls','accounts'), namespace='accounts')),
    path('', include(('sse_app.urls','sse_app'), namespace='sse_app')),
    path('', include(('admin_accounts.urls'), namespace='admin_accounts'))
]
