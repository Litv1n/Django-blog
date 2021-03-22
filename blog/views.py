from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-date')[:3]

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['title'] = 'Main blog page'
        return context


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['title'] = 'Blog page'
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['title'] = f'Recording - {Post.title}'
        return context
