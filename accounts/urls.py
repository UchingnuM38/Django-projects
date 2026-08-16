from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='job-list'), name='logout'),
    
    # Password Management
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password-change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password-change-done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password-reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password-reset-confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password-reset-complete'),
]
