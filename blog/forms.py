from django.forms import forms
from django.forms.models import ModelForm
from .models import CommentModel


class CommentModelForm(ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['post', 'created_at']
