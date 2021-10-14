from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    path('top', views.top, name='top'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('postsList', views.postsList, name='postsList'),
    path('activityDesc', views.activityDesc, name='activityDesc'),
    path('contactForm', views.contactForm, name='contactForm'),
    path('login', views.login, name='login'),
    path('postForm', views.postForm, name='postForm'),
]
