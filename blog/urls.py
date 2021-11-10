from django.urls import path
from . import views

urlpatterns = [

    path('', views.top, name='top'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('postsList', views.postsList, name='postsList'),
    path('<int:post_id>/', views.postsDetail, name='postsDetail'),
    path('activityDesc', views.activityDesc, name='activityDesc'),
    path('contactForm', views.contactForm, name='contactForm'),
    path('login', views.login, name='login'),
    path('postForm', views.postForm, name='postForm'),
    path('adminpostsList', views.adminPostsList, name='adminPostsList'),
    path('adminpostsregister/<int:pk>/', views.adminPostsRegister, name='adminPostsRegister'),
    path('adminPostsDelete/<int:pk>/', views.adminPostsDelete, name='adminPostsDelete'),

]
