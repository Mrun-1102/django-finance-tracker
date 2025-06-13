from django.urls import path
from .views import dashboard, register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
