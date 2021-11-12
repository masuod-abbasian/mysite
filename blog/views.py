from django.shortcuts import render
from blog.models import POST
# Create your views here.
def blog_view(request):
    return render(request,'blog/blog-home.html')

def blog_single(request):
    return render(request,'blog/blog-single.html')

def test(request):
    posts = POST.objects.all()
    context = {'posts': posts}
    return render(request,'test.html',context)