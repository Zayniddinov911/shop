from django.urls import path

from order.views import CheckoutView

app_name = 'order'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout')
]
