from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

me = User.objects.get(username='tsilvernail')

def post_list(request):
    posts = Post.objects.filter(author =me).order_by('author')
    return render(request, 'blog/post_list.html', {'posts': posts})
