from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "body", "created_date"]
    list_filter = ["title", "created_date"]
    search_fields = ["title", 'body', "created_date"]
    date_hierarchy = "created_date"
    ordering = ["title"]


admin.site.register(Post, PostAdmin)
