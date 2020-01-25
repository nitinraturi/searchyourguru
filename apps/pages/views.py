from django.shortcuts import render
from django.views.generic import TemplateView
from .mixins import AuthenticatedRedirectMixin, UnAuthenticatedRedirectMixin
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name="pages/home.html"

class LoginView(AuthenticatedRedirectMixin,TemplateView):
    template_name="account/login.html"
    redirect_url=reverse_lazy("pages:dashboard")

class SignupView(AuthenticatedRedirectMixin,TemplateView):
    template_name="account/signup.html"
    redirect_url=reverse_lazy("pages:dashboard")

class DashboardView(UnAuthenticatedRedirectMixin,TemplateView):
    template_name="pages/dashboard.html"
    redirect_url=reverse_lazy("pages:login")

class VerificationView(TemplateView):
    template_name="account/verification.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = self.request.GET.get('source')
        context['verification_email'] = self.request.GET.get('verification_email')
        return context

class PasswordResetView(TemplateView):
    template_name="account/password_reset.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
