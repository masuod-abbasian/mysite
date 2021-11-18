from django.shortcuts import get_list_or_404, render, get_object_or_404
from blog.models import POST
import datetime
# Create your views here.
def blog_view(request):
    posts = POST.objects.filter(status=1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post = POST.objects.filter(status=1)
    posts = get_object_or_404(post, pk=pid)
    post_index = list(post.values_list('pk',flat=True))
    # post_index = list(POST.objects.filter(status=1))
    # pid = int(pid)
    post_i = post_index.index(pid)
    # if post_i <= len(post_index):
    
    id_next = post_index[post_i+1]
    
    # else:
        # id_next = pid
    # if post_i > len(post_index)-1 and post_i <= 0:
    
    id_prev = post_index[post_i-1]
    # else:
    #     id_prev = pid
    
    # else:
        # id_prev = pid

    
    


    
    context = {'post': posts,'id_next': id_next, 'id_prev': id_prev}
    


    # posts = get_object_or_404(POST, pk=pid)
    # posts.counted_view += 1 
    # posts.save()
    # context = {'posts': posts}
   
    return render(request,'blog/blog-single.html',context)

def test(request):
    # post = POST.objects.get(id=pid)
    # post = get_object_or_404(POST, pk=pid)
    # context = {'post': post}
    # return render(request,'test.html',context)
    postt = POST.objects.filter(status=1)
    
    context = {'poste': postt}
    return render(request,'test.html',context)