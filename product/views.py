from django.shortcuts import render, redirect, get_object_or_404
from .models import WishlistModel
from django.contrib.auth.decorators import login_required
from shop.models import ProductModel


@login_required
def update_wishlist(request, pk):
    product = get_object_or_404(ProductModel.objects.all().filter(id=pk))
    wishlist = WishlistModel.add_to_delete(request.user, product)

    return redirect('shop:shop')

