from django.shortcuts import render,redirect
from .froms import CategoryForm
# Create your views here.
def add_category(request):
    if request.method=='POST':
        category_form= CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('/')
    else:
        category_form= CategoryForm(request.POST)
    return render(request,'add_category.html',{'form':category_form})