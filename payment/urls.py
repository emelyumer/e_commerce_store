from django.urls import path

from views import checkout, complete_order, payment_success, payment_failed


urlpatterns = [

    path('checkout', checkout, name='checkout'),
    path('complete-order', complete_order, name='complete-order'),
    path('payment-success', payment_success, name='payment-success'),
    path('payment-failed', payment_failed, name='payment-failed'),

]








