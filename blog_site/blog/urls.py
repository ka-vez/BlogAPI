from django.urls import path
from . import views
urlpatterns = [
    path('', views.blogpost.as_view(), name='blog_post'),
    path('post/<int:pk>/', views.post.as_view(), name='post'),
    path('filter/', views.filter_blog),
    path('secret/', views.secret)

]