"""qr_stlarx URL Configuration

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
from django.urls import include, path, re_path
import accounts
from accounts import views

urlpatterns = [
    path('', include('homepage.urls')),
    path('qr-gen/', include('qr_generator.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login_view, name='login'),
    path('logout/', accounts.views.logout_view, name='logout'),
    path('viewer/', include('viewer.urls')),
    # re_path(r'^captcha/', include('captcha.urls')),
]
