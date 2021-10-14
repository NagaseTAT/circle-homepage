from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
# from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def top(request):
    return render(request, 'blog/Top.html', {})

def portfolio(request):
    return render(request, 'blog/Portfolio.html', {})

def postsList(request):
    return render(request, 'blog/PostsList.html', {})

def activityDesc(request):
    return render(request, 'blog/ActivityDescription.html', {})

def contactForm(request):
    return render(request, 'blog/ContactForm.html', {})

def login(request):
    return render(request, 'blog/Login.html', {})

def postForm(request):
    return render(request, 'blog/PostForm.html', {})
# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
