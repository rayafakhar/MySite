from django.urls import path
from website.views import blog_home_view, blog_single_view

app_name = 'blog'

urlpatterns = [
    path('home/', blog_home_view, name='blog_home'),
    path('single/', blog_single_view, name='blog_single'),
]
