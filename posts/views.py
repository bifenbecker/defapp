from django.shortcuts import render
from django.views import View

from .models import *


class ListPostsView(View):
    template_name = 'posts.html'
    context = {
        'page_title': 'Посты'
    }

    def get(self, request):
        posts = Post.objects.all()
        self.context.update({'posts' :posts})
        return render(request, self.template_name, self.context)


class PostDetailView(View):
    template_name = 'post_detail.html'
    context = {
        'page_title': 'Пост'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
