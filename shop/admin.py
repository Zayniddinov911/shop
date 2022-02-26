from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from .forms import ColorModelForm


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['created_at']
    autocomplete_fields = ['tag', 'category']
    readonly_fields = ['real_price']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'created_at', 'color']
    list_display_links = ['id', 'code']
    form = ColorModelForm

    def color(self, obj):
        return mark_safe(f'<div style="background-color:{obj.code}; width:50px; height:20px;"></div>')


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
