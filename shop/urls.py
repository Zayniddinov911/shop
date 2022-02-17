from django.urls import path
from .views import ShopView, ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('<int:pk>/details/', ProductDetailView.as_view(), name='product_detail'),
]