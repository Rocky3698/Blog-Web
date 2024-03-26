from django.shortcuts import render,redirect
from .forms import ProfileForm
# Create your views here.
def creat_profile(request):
    if request.method=='POST':
        profile_form=ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/')
    else:
        profile_form=ProfileForm(request.POST)    
    return render(request,'creat_profile.html',{'form':profile_form})