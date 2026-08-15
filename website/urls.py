from django.urls import path
from website.views import *
urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about' ),
    path('contact', contact_view, name='contact'),
    path('elements', elements_view, name='elements'),
    path('blog-home', blog_home_view, name='blog_home'),
    path('blog-single', blog_single_view, name='blog_single'),
]