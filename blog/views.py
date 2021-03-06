from django.shortcuts import render, get_object_or_404,redirect
from blog.models import POST,Comment
import datetime
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# @login_required
def blog_view(request,**kwargs):
    posts = POST.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])
    
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited succsesfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment didnt submited ')
    post = POST.objects.filter(status=1)
    posts = get_object_or_404(post,pk=pid)
    if not posts.login_require:
        comments = Comment.objects.filter(post = posts.id,approved=True)
        form = CommentForm()
        prev = POST.objects.filter(id__lt=posts.id).order_by('-id').first()
        if prev == None:
            prev_post = posts
        else:
            prev_post = prev
        
        #     prev = POST.objects.filter(id__lt=posts.id).order_by('-id').first()
        #     prev_post = get_object_or_404(prev)
        
        next = POST.objects.filter(id__gt=posts.id).order_by('id').first()
        if next == None:
            next_post = posts
        else:
            next_post = next
        
        #     next = POST.objects.filter(id__gt=posts.id).order_by('id').first()
        #     next_post = get_object_or_404(next)
        # prev_post = posts.get_next_by_id()
        # next_post = posts.get_previous_by_date()

            
        context = {'post': posts,'prev_post': prev_post, 'next_post':next_post, 'comments':comments,'form':form}
        


        # posts = get_object_or_404(POST, pk=pid)
        # posts.counted_view += 1 
        # posts.save()
        # context = {'posts': posts}
    
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))



def test(request):
    # post = POST.objects.get(id=pid)
    # post = get_object_or_404(POST, pk=pid)
    # context = {'post': post}
    return render(request,'test.html')
    # postt = POST.objects.filter(status=1)
    
    # context = {'poste': postt}
    # return render(request,'test.html',context)

# def blog_category(request,cat_name):
#     posts = POST.objects.filter(status=1)
#     posts = posts.filter(category__name=cat_name)
#     context = {'posts': posts}
#     return render(request,'blog/blog-home.html',context)

def blog_search(request):
    # print(request.__dict__)
    posts = POST.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)



