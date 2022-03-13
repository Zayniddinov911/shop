from django.shortcuts import render
from django.views.generic import CreateView

from order.forms import OrderModelForm
from order.models import OrderModel
from shop.models import ProductModel


class CheckoutView(CreateView):
    template_name = 'main/checkout.html'
    form_class = OrderModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        context['product'] = ProductModel.get_cart_info(cart)

        # if hasattr(self.request.user.profile):
        #     # context['profile'] = self.request.user.profile
        return context
