from django.shortcuts import render , redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def creat_post(request):
    if request.method =='POST':
        post_form=PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect('/')
    else:
        post_form=PostForm(request.POST)
    return render(request,'creat_post.html',{'form':post_form})

def edit_post(request, id):
    post = Post.objects.get(pk=id)
    post_form=PostForm(instance=post)
    if request.method =='POST':
        post_form=PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('/')
    
    return render(request,'creat_post.html',{'form':post_form})

def delete_post(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
