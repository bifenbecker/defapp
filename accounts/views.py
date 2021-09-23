from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View

from .forms import *


class LoginPageView(LoginView):
    template_name = 'login.html'
    extra_context = {
        'page_title': 'Логин'
    }
    authentication_form = LoginForm



class RegistrationPageView(View):
    template_name = "registration.html"
    context = {
        'page_title': 'Регистрация'
    }

    def get(self, request):
        form = RegistrationForm(request.POST or None)
        self.context.update({'form': form})
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = form.cleaned_data['email']
            new_user.username = form.cleaned_data['email'].split("@")[0]
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('main_page_url')

        self.context.update({'form': form })
        return render(request, self.template_name, context=self.context)


class ProfileView(View):
    template_name = "profile.html"
    context = {
        'page_title': 'Мой профиль'
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)
