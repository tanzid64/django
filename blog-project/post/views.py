from django.shortcuts import render
from post.models import Post, Comment
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from post.forms import PostForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from post.forms import CommentForm

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
  def post(self, request, *args, **kwargs):
    comment_form = CommentForm(data=self.request.POST)
    post = self.get_object()
    if comment_form.is_valid():
      comment = comment_form.save(commit=False) # Comment object created but not saved in database
      comment.user = self.request.user # Fill out this field in comment object
      comment.post = post # Fill out this field in comment object
      comment.save() # Finally seve the object in the database
    return self.get(request, *args, **kwargs)
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    current_post = self.get_object() # Current Post
    comments = Comment.objects.filter(post=current_post) # Ei post er jonno shob comment, Comment model theke query kore niye ashlam
    context['comments'] = comments
    return context
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

# class PostCommentView(CreateView):
#   template_name = 'postDetail.html'
#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     messages.success(self.request, "Post created successfully")
#     return super().form_valid(form)