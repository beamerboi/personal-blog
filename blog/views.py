from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, "blog/home.html", {'blogs':blogs})

def blog_detail(request, id_blog):
    blog = get_object_or_404(Blog, pk=id_blog)
    return render(request, 'blog/blog_detail.html',{'blog':blog})
