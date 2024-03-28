from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
# def add_author(request):
#     if request.method=='POST':
#         author_form= forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('/profile/creat/')
#     else:
#         author_form= forms.AuthorForm(request.POST)    
#     return render(request,'add_author.html',{'form':author_form})

def register(request):
    if request.method=='POST':
        register_form= RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('register')
    else:
        register_form= RegistrationForm(request.POST)    
    return render(request,'register.html',{'form':register_form,'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form= AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name= form.cleaned_data['username']
            user_pass= form.cleaned_data['password']
            user= authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Logged in successfully')
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,'Invalid Information Enterd')
                return redirect('register')
    else:
        form= AuthenticationForm(request,request.POST)
        return render(request,'register.html',{'form':form, 'type':'Login'})