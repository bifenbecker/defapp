from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # Изменен путь до админки
    path('/def/pass/admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('main/', MainPageReDirect.as_view(), name='main_page_url'),
    path('posts/', include('posts.urls')),
]
