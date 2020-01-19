from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name="pages/home.html"

class LoginView(TemplateView):
    template_name="account/login.html"

class SignupView(TemplateView):
    template_name="account/signup.html"
