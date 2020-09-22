"""t4tt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import settings
from accounts import views as account_views
from main_app import urls as main_app_urls
from main_app import views as main_app_views


urlpatterns = [
    path('home/', include('main_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('main_app/', include('main_app.urls')),
    path('',account_views.signin),
    path('check_cli_num/', main_app_views.check_cli_num, name='check_cli_num'),
    #path('main_app/dashboard',main_app_views.dashboard)
    ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # method that allows media url
