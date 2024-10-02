from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(TemplateView):
    template_name = 'AJV_blog/Post_list.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_posts"] = Post.objects.all()[:5]
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'AJV_blog/Post_create.html' 
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

class PostUpdateView(UpdateView):  
    model = Post
    template_name = 'AJV_blog/Post_update.html' 
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

class PostDeleteView(DeleteView):  
    model = Post
    template_name = 'AJV_blog/Post_delete.html' 
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')