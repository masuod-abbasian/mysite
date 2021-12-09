from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import POST
from website.models import Contact
from website.forms import NameForm ,Contactform, Newsletterform
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')
    
def contact_view(request):
    if request.method == 'POST':
        form = Contactform(request.POST,)
        
        
        if form.is_valid():
            # form.cleaned_data['name'] = 'bbbbb'
            # form.initial['name'] ='sssss'
            # form.changed_data['name']= 'qqqqq'
            # print(form.initial)
            # print(form.changed_data)
            # print(form)
            # print(form.cleaned_data)
            # form['name'].name = 'bbbbbb'
            
            # form['name']
            post = form.save(commit=False)
            post.name = 'na shenas'
            post.save()
            
            messages.add_message(request,messages.SUCCESS,'your ticket submited succsesfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submited')
    form = Contactform() 
    
    return render(request, 'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
def about_view(request):
    return render(request, 'website/about.html')

def test_view(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # subject = form.cleaned_data['subject']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # print(name, subject, email, message)
            return HttpResponse('done')
        else:
            return HttpResponse('Not valid')


        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # subject=request.POST.get('subject')
        # message=request.POST.get('message')
        # c = Contact()
        # c.name=name
        # c.email=email
        # c.subject=subject
        # c.massage=message
        # c.save()
        # print(name)

    form = Contactform()
    return render(request, 'test.html',{'form':form})