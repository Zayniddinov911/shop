from django.contrib import admin

from order.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    list_display_links = ['id', 'user', 'created_at']
    search_fields = ['user', 'created_at']
