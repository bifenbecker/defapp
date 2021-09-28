from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ListPostsView.as_view(), name='posts_view_url'),
    path('<int:post_id>', PostDetailView.as_view(), name='posts_view_url'),
]
