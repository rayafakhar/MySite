from django.shortcuts import render
from django.http import HttpResponse,JsonResponse 

def index_view(request):
    return render(request , 'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')

def elements_view(request):
    return render(request, 'website/elements.html')

def blog_home_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single_view(request):
    return render(request, 'blog/blog-single.html')


