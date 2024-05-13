from django import forms
from post.models import Post
from post.models import Comment


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'content')


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']