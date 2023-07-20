"""ltcs URL Configuration

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
from django.contrib import admin
<<<<<<< HEAD:long_tern_care/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from long_tern_care_api import views
from django.views.generic import RedirectView
=======
from django.urls import include, path
from rest_framework import routers
>>>>>>> dev:ltcs/ltcs/urls.py

from accounts import views

router = routers.SimpleRouter(trailing_slash=False)
router.register('users', views.UserViews, basename='users')

urlpatterns = [
<<<<<<< HEAD:long_tern_care/urls.py
    path(r'admin/', admin.site.urls),
    path(r'api', include(router.urls)),
    path('login', views.LoginView.as_view(), name='login'),
    path('api/users/create', views.UserCreateView.as_view(), name='user-create'),
    #path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
=======
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('token', views.TokenView.as_view())
>>>>>>> dev:ltcs/ltcs/urls.py
]
