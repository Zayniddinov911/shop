from django.db.models.signals import pre_save
from django.dispatch import receiver

from shop.models import ProductModel


@receiver(pre_save, sender=ProductModel)
def real_price_get(sender, instance, *args, **kwargs):

    if instance.is_discount():
        instance.real_price = instance.price - (instance.price / 100) * instance.discount
    else:
        instance.real_price = instance.price

