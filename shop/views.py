from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


class ShopView(ListView):
    model = ProductModel
    paginate_by = 3
    template_name = 'main/shop.html'

    def get_queryset(self):
        return ProductModel.objects.order_by('-pk')


class ProductDetailView(DetailView):
    template_name = 'main/product_detail.html'
    model = ProductModel
