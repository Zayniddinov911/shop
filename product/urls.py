from django.urls import path
from .views import update_wishlist, WishlistView, update_cart, CartListView

app_name = 'products'

urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('<int:pk>/wishlist/', update_wishlist, name='add_wishlist'),
    path('<int:pk>/cart/', update_cart, name='add_cart'),
    path('Shopping/cart/', CartListView.as_view(), name='shop_cart'),
]