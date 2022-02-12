from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCommentView

app_name = 'blogs'

urlpatterns = [
    path('<int:pk>/comments/', BlogCommentView.as_view(), name='blog_comments'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/post-details/', BlogDetailView.as_view(), name='blog_detail')
]

