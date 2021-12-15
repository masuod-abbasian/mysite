from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.forms import signupform
from accounts.backends import EmailBackend

# Create your views here.
# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             sign = signupform(request.POST)
           
#             if sign.is_valid():
#                 sign.save()
#             form = AuthenticationForm(request=request, data=request.POST)
#             print(form)
#             if form.is_valid():
#                 # email = form.cleaned_data.get('email')
#                 username = form.cleaned_data.get('username')
#                 password = form.cleaned_data.get('password')
#                 # print(email)
#                 print(username)
#                 user = AuthenticationForm(request, username=username, password=password)
                
#                 print(user)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('/')
        
#         form = EmailBackend()
#         context = {'form':form}
#     # if request.user.is_authenticated:
#     #     msg = f'user is authenticated as {request.user.username}'
#     # else:
#     #     msg = 'user is not authenticated'
#     # {'msg':msg}
#         return render(request, 'accounts/login.html',context)
#     else:
#         return redirect('/')

# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = signupform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = signupform()
        context = {'form':form}
        return render(request, 'accounts/signup.html',context)
    else:
        return redirect('/')