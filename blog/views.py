from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
# from .forms import PostForm
from .forms import PostForm
from . import forms
from django.shortcuts import redirect
from blog.models import *
from django.template.context_processors import csrf
from django.http import Http404
import datetime
# Create your views here.

def top(request):
    return render(request, 'blog/Top.html', {})

def portfolio(request):
    users = User.objects.all
    posts = Post.objects.all
    tags = Tag.objects.all
    return render(request, 'blog/Portfolio.html', {'users': users, 'posts': posts, 'tags': tags})

def paginate_query(request, queryset, count):
  paginator = Paginator(queryset, count)
  page = request.GET.get('page')
  try:
    page_obj = paginator.page(page)
  except PageNotAnInteger:
    page_obj = paginator.page(1)
  except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)
  return page_obj

def postsList(request):
    posts = Post.objects.order_by('created_date')
    page_obj = paginate_query(request, posts, settings.PAGE_PER_ITEM)
    return render(request, 'blog/PostsList.html', {'page_obj': page_obj})

def postsDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/postsDetail.html', {'post':post})

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
        # titleの入力が空でなければ投稿を登録する
        if params['title'] != '':
            new_post = Post()
            new_post.title = params['title']
            new_post.text = params['text']
            new_post.author_id = params['on_user']
            new_post.save()
            # チェックされたタグを取得し、tagテーブルに登録
            for t in params['tag']:
                Tag(user_id=int(t), post_id=new_post.id).save()
        return redirect(adminPostsList)
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

def adminPostsList(request):
    user_id = 1
    # ログインユーザの書いた投稿データのみpostsに代入
    posts = Post.objects.order_by('created_date').reverse().filter(author_id=user_id)
    return render(request, 'blog/AdminPostsList.html', {'posts':posts})

def adminPostsRegister(request, pk):
    try:
        posts = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404

    if request.method == "POST":
        posts.title = request.POST["title"]
        posts.text = request.POST["text"]
        tags = request.POST.getlist("tag")
        date = datetime.datetime.now()
        if posts.title != '':
            posts.save()
            # この投稿についているタグを一度全消去
            Tag.objects.filter(post_id=posts.id).delete()
            # チェックされたタグを取得、tagテーブルに登録
            for t in tags:
                Tag(user_id=int(t), post_id=posts.id).save()

        return redirect(adminPostsList)
    else:
        # placeholder設定のため以下２行
        initial_dict = dict(title=posts.title, text=posts.text)
        form = PostForm(request.GET or None, initial=initial_dict)

        tags = User.objects.all()
        choice = []
        for tag in tags:
            choice.append((tag.id, tag.username))
        form.fields['tag'].choices = choice

        return render(request, 'blog/AdminPostsRegister.html', dict(form=form))

def adminPostsDelete(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    post.delete()
    return redirect(adminPostsList)