from django.shortcuts import render
from post.models import Post
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from post.forms import PostForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class CreatePostView(LoginRequiredMixin, CreateView):
  template_name = 'createPost.html'
  form_class = PostForm
  success_url = reverse_lazy('index')

  def form_valid(self, form):
    form.instance.author = self.request.user
    messages.success(self.request, "Post created successfully")
    return super().form_valid(form)
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Create a Post'
    context['button'] = 'Create'
    return context
  
class PostDetailView(DetailView):
  model = Post
  template_name = 'postDetail.html'
  context_object_name = 'post'
  lookup_field = 'slug'

class UpdatePostView(LoginRequiredMixin,UpdateView):
  queryset = Post.objects.all()
  form_class = PostForm
  template_name = 'createPost.html'
  lookup_up = 'slug'
  success_url = reverse_lazy('index')

  def form_valid(self, form):
      messages.success(self.request, "Post updated successfully")
      return super().form_valid(form)
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Update Post'
    context['button'] = 'Update'
    return context

class DeletePostView(DeleteView):
  model = Post
  queryset = Post.objects.all()
  lookup_field = 'slug'
  success_url = reverse_lazy('index')

