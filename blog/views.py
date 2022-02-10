from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPostModel


class BlogListView(ListView):
    model = BlogPostModel
    # queryset = BlogPostModel.objects.order_by('-pk')
    template_name = 'main/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = BlogPostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        if tag:
            return qs.filter(tags__title=tag)
        else:
            return qs


class BlogDetailView(DetailView):
    model = BlogPostModel
    template_name = 'main/blog_detail.html'
    context_object_name = 'posts'
