from django.contrib.auth.views import (LogoutView, LoginView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)
from django.urls import path
from .views import *
app_name = 'users'

urlpatterns = [
    path('', index, name = 'main'),
    path('signup/', SignUp.as_view(), name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout',
    ),
    path('signup/', SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path('password_change/',
         PasswordChangeView.as_view(
             template_name='users/password_change_form.html'),
         name='password_change',
     ),
    path('password_change/done',
         PasswordChangeDoneView.as_view(
             template_name='users/password_change_done.html'),
         name='password_change_done',
     ),
    path(
        'user/<int:user_id>',
        user,
        name='user',
     ),
    path(
        'help',
        help,
        name='help',
     ),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
]
