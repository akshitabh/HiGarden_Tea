from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
def home(request):
    item=Product.objects.all()
    return render(request,'home.html',{'item':item})
def about(request):
    return render(request,'about.html')
def contact(request):
         detail=Person.objects.all()
         return render(request,'contact.html',{'detail':detail})
    
def contact_us(request):
    if request.method=='POST':
        pname=request.POST['name']
        pemail=request.POST['email']
        psub=request.POST['subject']
        pmessage=request.POST['message']
        if Person.objects.filter(email = pemail).exists():
            messages.error(request,'email already exist')
            return redirect('/contact/')   
        else:
            Person.objects.create(name=pname,email=pemail,subject=psub,message=pmessage)
            messages.success(request,'person successfully added')
            detail=Person.objects.all()
            return render(request,'contact.html',{'detail':detail})
    
# Create your views here.
