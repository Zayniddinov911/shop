from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/post-details/', BlogDetailView.as_view(), name='blog_detail')
]