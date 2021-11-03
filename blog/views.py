from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from . import forms
from django.shortcuts import redirect
from blog.models import *
from django.template.context_processors import csrf

# Create your views here.

def top(request):
    return render(request, 'blog/Top.html', {})

def portfolio(request):
    users = User.objects.all
    posts = Post.objects.all
    tags = Tag.objects.all
    return render(request, 'blog/Portfolio.html', {'users': users, 'posts': posts, 'tags': tags})

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
    user_id = 1
    params = {'title': '', 'on_user': user_id, 'text': '', 'tag': '', 'form': None}
    if request.method == 'POST':
        form = PostForm(request.POST)
        params['title'] = request.POST['title']
        params['text'] = request.POST['text']
        params['tag'] = request.POST.getlist("tag")
        params['form'] = form
        if params['title'] != '':
            new_post = Post()
            new_post.title = params['title']
            new_post.text = params['text']
            new_post.author_id = params['on_user']
            new_post.save()
            for t in params['tag']:
                Tag(user_id=int(t), post_id=new_post.id).save()
        return redirect(postsList)
    else:
        form = forms.PostForm()

        tags = User.objects.all()
        choice = []
        for tag in tags:
            choice.append((tag.id, tag.username))
        form.fields['tag'].choices = choice
        params['form'] = form
        # # CFRF対策（必須）
        params.update(csrf(request))
    return render(request, 'blog/PostForm.html', params)
