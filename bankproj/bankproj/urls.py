"""
URL configuration for bankproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
# banking_project/urls.py
from django.contrib import admin
from django.urls import include, path

from bankapp.views import register_user, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banking/', include('bankapp.urls')),
    path('accounts/', include('bankapp.urls')),
    path('register/', register_user, name='register_user'),
    path('login/', user_login, name='login'),
    # path('get_branches/<int:district_id>/', get_branches, name='get_branches'),
]

if settings.DEBUG:
    urlpatterns+=static( settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)