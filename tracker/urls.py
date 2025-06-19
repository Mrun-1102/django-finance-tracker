from django.urls import path
from .views import dashboard, register_view, add_income, add_expense
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add-income/', add_income, name='add_income'),
    path('add-expense/', add_expense, name='add_expense'),
    path('income/edit/<int:pk>/', views.edit_income, name='edit_income'),
    path('income/delete/<int:pk>/', views.delete_income, name='delete_income'),
    path('expense/edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('expense/delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('set-budget/', views.set_budget, name='set_budget'),
    path('download-csv/', views.download_csv, name='download_csv'),
    # path('dashboard/category-data/', expense_category_data, name='expense_category_data'),
    # path('dashboard/monthly-data/', monthly_expense_data, name='monthly_expense_data'),


]
