from django.urls import path
from account.views import register, email_verification, email_verification_failed, email_verification_sent, email_verification_success


urlpatterns = [
    path('register/', register, name='register'),
    path('email-verification/', email_verification, name='email-verification'),
    path('email-verification-failed/', email_verification_failed, name='email-verification-failed'),
    path('email-verification-sent/', email_verification_sent, name='email-verification-sent'),
    path('email-verification-success/', email_verification_success, name='email-verification-success'),
]