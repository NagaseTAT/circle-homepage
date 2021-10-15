from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
# from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def top(request):
    return render(request, 'blog/Top.html', {})

def portfolio(request):
    return render(request, 'blog/Portfolio.html', {})

def postsList(request):
    return render(request, 'blog/PostsList.html', {})

def postsDetail(request):
    return render(request, 'blog/postsDetail.html', {})

def activityDesc(request):
    return render(request, 'blog/ActivityDescription.html', {})

def contactForm(request):
    return render(request, 'blog/ContactForm.html', {})

def login(request):
    return render(request, 'blog/Login.html', {})

def postForm(request):
    return render(request, 'blog/PostForm.html', {})

