from django.urls import path
from . import views

urlpatterns = [

    path('', views.top, name='top'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('postsList', views.postsList, name='postsList'),
    path('postsDetail', views.postsDetail, name='postsDetail'),
    path('activityDesc', views.activityDesc, name='activityDesc'),
    path('contactForm', views.contactForm, name='contactForm'),
    path('login', views.login, name='login'),
    path('postForm', views.postForm, name='postForm'),
]
