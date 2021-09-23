from django.shortcuts import render, redirect
from django.views import View

class MainPageReDirect(View):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
