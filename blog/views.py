# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.shortcuts import render
from django.utils import timezone
# Create your views here.

#def post_list(request):
   # return render(request, 'blog/post_list.html', {})
    
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})
    