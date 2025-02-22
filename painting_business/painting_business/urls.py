"""painting_business URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main_app.views import *
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop',home_view,name = 'shop'),
    path('shop/<slug:slug>',product_view,name = 'product'),
    path('',index_view,name='home'),
    path('register/',register_view,name='register'),
    path('login/',login_view,name = 'login'),
    path('logout/',logout_view,name = 'logout')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
