from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.models import ProductModel

UserModel = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='orders', verbose_name=_('user'))
    total_price = models.FloatField(verbose_name=_('total price'))
    product = models.ManyToManyField(ProductModel)

    first_name = models.CharField(max_length=50, verbose_name=_('first name'))
    last_name = models.CharField(max_length=50, verbose_name=_('last name'))
    country = models.CharField(max_length=25, verbose_name=_('country'))
    address1 = models.CharField(max_length=100, verbose_name=_('address 1'))
    address2 = models.CharField(max_length=100, verbose_name=_('address 2'), blank=True, null=True)
    city = models.CharField(max_length=25, verbose_name=_('city'))
    state = models.CharField(max_length=25, verbose_name=_('state'))
    zip_code = models.CharField(max_length=6, verbose_name=_('zip code'))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    email = models.EmailField(verbose_name=_('email'))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.total_price}' #Temporary

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'



