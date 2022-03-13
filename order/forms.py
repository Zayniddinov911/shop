from django import forms

from order.models import OrderModel


class OrderModelForm(forms.ModelForm):

    class Meta:
        model = OrderModel
        exclude = ['user', 'product', 'total_price', 'created_at']