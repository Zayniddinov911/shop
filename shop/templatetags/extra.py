from django import template
from product.models import WishlistModel
register = template.Library()


@register.simple_tag()
def get_current_price(request, x):
    t = request.GET.get('price')
    if t:
        return t.split(';')[x]
    else:
        return 'null'


@register.filter
def is_wishlist(product, user):
    return WishlistModel.objects.filter(user=user, product=product).exists()
