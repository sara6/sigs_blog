from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    # order_by('publised_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
