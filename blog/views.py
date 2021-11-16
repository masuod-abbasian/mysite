from django.shortcuts import render, get_object_or_404
from blog.models import POST
import datetime
# Create your views here.
def blog_view(request):
    posts = POST.objects.filter(status=1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = POST.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    # posts = get_object_or_404(POST, pk=pid)
    # posts.counted_view += 1 
    # posts.save()
    # context = {'posts': posts}
   
    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    # post = POST.objects.get(id=pid)
    post = get_object_or_404(POST, pk=pid)
    context = {'post': post}
    return render(request,'test.html',context)