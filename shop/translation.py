from modeltranslation.translator import translator, TranslationOptions, register
from .models import ProductModel
# from .templatetags.extra import register


@register(ProductModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('short_description', 'long_description')


