from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include


urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')), 
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout',
    ),
]
