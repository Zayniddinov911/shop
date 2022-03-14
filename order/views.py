from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from order.forms import OrderModelForm
from order.models import OrderModel
from shop.models import ProductModel


class CheckoutView(CreateView):
    template_name = 'main/checkout.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('order:history')   #/order/history #reverse order:history nomidagi url text formatga otqazib beradi

    def form_valid(self, form):
        cart = self.request.session.get('cart', [])
        products = ProductModel.get_cart_info(cart)

        form.instance.user = self.request.user
        form.instance.price = products.aggregate(
            Sum('real_price')
        )['real_price__sum']

        orders = form.save()

        orders.products.set(products)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        context['product'] = ProductModel.get_cart_info(cart)

        if hasattr(self.request.user, "profile"):
            context['profile'] = self.request.user.profile

        return context


class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'main/order_history.html'

    def get_queryset(self):
        return self.request.user.orders.all()
