from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class TagModel(models.Model):
    name = models.CharField(max_length=55, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    short_description = models.TextField(verbose_name=_('short description'))
    long_description = models.TextField(verbose_name=_('long description'))
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.RESTRICT,
        related_name='products',
        verbose_name=_('category')
    )
    tag = models.ManyToManyField(
        TagModel,
        related_name='products',
        verbose_name=_('tag')

    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def get_price(self):
        if self.discount == 0:
            return self.price
        # return ((100 - self.discount) / 100) * self.price   # both of calculations are correct
        return self.price - (self.price / 100) * self.discount  # both of calculations are correct

    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3

    def is_discount(self):
        return self.discount != 0

    def get_related(self):
        return ProductModel.objects.filter(category__name=self.category).exclude(pk=self.pk)[:3]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
