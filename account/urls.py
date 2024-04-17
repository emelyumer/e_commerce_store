from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.urls import path
from account.views import (register, email_verification, email_verification_failed, email_verification_sent,
                           email_verification_success, my_login, user_logout, dashboard, profile_management,
                           delete_account, manage_shipping, track_orders)


urlpatterns = [
    path('register/', register, name='register'),
    path('email-verification/<str:uidb64>/<str:token>/', email_verification, name='email-verification'),
    path('email-verification-failed/', email_verification_failed, name='email-verification-failed'),
    path('email-verification-sent/', email_verification_sent, name='email-verification-sent'),
    path('email-verification-success/', email_verification_success, name='email-verification-success'),
    # Login / logout urls

    path('my-login', my_login, name='my-login'),

    path('user-logout', user_logout, name='user-logout'),

    # Dashboard / profile urls

    path('dashboard', dashboard, name='dashboard'),

    path('profile-management', profile_management, name='profile-management'),

    path('delete-account', delete_account, name='delete-account'),

    # Password management urls/views

    # 1 ) Submit our email form

    path('reset_password', PasswordResetView.as_view(template_name="account/password/password-reset.html"),
         name='reset_password'),

    # 2) Success message stating that a password reset email was sent

    path('reset_password_sent',
         PasswordResetDoneView.as_view(template_name="account/password/password-reset-sent.html"),
         name='password_reset_done'),

    # 3) Password reset link

    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name="account/password/password-reset-form.html"),
         name='password_reset_confirm'),

    # 4) Success message stating that our password was reset

    path('reset_password_complete',
         PasswordResetCompleteView.as_view(template_name="account/password/password-reset-complete.html"),
         name='password_reset_complete'),

    # Manage shipping url

    path('manage-shipping', manage_shipping, name='manage-shipping'),

    # Track orders url

    path('track-orders', track_orders, name='track-orders'),

]