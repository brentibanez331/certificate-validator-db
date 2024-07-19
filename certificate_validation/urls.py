"""
URL configuration for certificate_validation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import re_path, path
from apis.views import auth_views
from apis.views import user_views

urlpatterns = [
    re_path('login', auth_views.login),
    re_path('signup', auth_views.signup),
    re_path('test_token', auth_views.test_token),
    re_path('users/search', user_views.get_users),
    path('users/remove/<str:person_user_id>/', user_views.delete_user, name='delete_user'),
    path('admin/', admin.site.urls),
]
