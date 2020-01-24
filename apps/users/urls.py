from django.contrib.auth import views as auth_views
from django.urls import path,re_path,include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = "apps.users"
router = DefaultRouter()
router.register(r'', AuthViewSet,basename="auth")
router.register(r'', UserViewSet,basename="user")

urlpatterns = [
    path('', include(router.urls)),
    re_path('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate_account, name='activate_account'),
    re_path('^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_verification, name='password_reset_verification'),
]

# urlpatterns += [
    # path('login/',
    #      auth_views.LoginView.as_view(),
    #      name='login'),
    # path('logout/',
    #      auth_views.LogoutView.as_view(),
    #      name='logout'),
    # path('password-change/',
    #      auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password-change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),
    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password-reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),
# ]
