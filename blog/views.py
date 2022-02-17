from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import CommentModelForm
from .models import BlogPostModel, CommentModel


#

class BlogListView(ListView):
    model = BlogPostModel
    # queryset = BlogPostModel.objects.order_by('-pk')
    template_name = 'main/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 2

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

#


class BlogCommentView(CreateView):
    model = CommentModel
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(BlogPostModel, id=self.kwargs.get('pk'))
        return super(BlogCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.kwargs.get('pk')})
