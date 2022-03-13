from django.db.models import Min, Max
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


class ShopView(ListView):
    model = ProductModel
    paginate_by = 3
    template_name = 'main/shop.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShopView, self, **kwargs).get_context_data()
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = TagModel.objects.all()
        context['size'] = SizeModel.objects.all()
        context['color'] = ColorModel.objects.all()

        context['min_price'], context['max_price'] = ProductModel.objects.aggregate(
            Min('real_price'),
            Max('real_price')).values()

        return context

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__contains=q)
            return qs

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category_id=cat)
            # return qs

        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tag__id=tag)
            # return qs

        size = self.request.GET.get('size')
        if size:
            qs = qs.filter(size__id=size)

        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(color_id=color)

        price_sort = self.request.GET.get('price_sort')
        if price_sort == 'price':
            qs = qs.order_by('real_price')
        elif price_sort == '-price':
            qs = qs.order_by('-real_price')

        price = self.request.GET.get('price')
        if price:
            min, max = price.split(';')
            qs = qs.filter(real_price__gte=min, real_price__lte=max)

        return qs


class ProductDetailView(DetailView):
    template_name = 'main/product_detail.html'
    model = ProductModel

