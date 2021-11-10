from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
# from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def top(request):
    return render(request, 'blog/Top.html', {})

def portfolio(request):
    return render(request, 'blog/Portfolio.html', {})

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
    return render(request, 'blog/PostForm.html', {})

