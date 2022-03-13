from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_('first name'), blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name=_('last name'), blank=True, null=True)
    country = models.CharField(max_length=25, verbose_name=_('country'), blank=True, null=True)
    address1 = models.CharField(max_length=100, verbose_name=_('address 1'), blank=True, null=True)
    address2 = models.CharField(max_length=100, verbose_name=_('address 2'), blank=True, null=True)
    city = models.CharField(max_length=25, verbose_name=_('city'), blank=True, null=True)
    state = models.CharField(max_length=25, verbose_name=_('state'), blank=True, null=True)
    zip_code = models.CharField(max_length=6, verbose_name=_('zip code'), blank=True, null=True)
    phone = models.CharField(max_length=13, verbose_name=_('phone'), blank=True, null=True)
    email = models.EmailField(verbose_name=_('email'), blank=True, null=True)

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name=_('user'), related_name='profile')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
