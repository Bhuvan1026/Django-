from django.shortcuts import render
from django.contrib import messages
from .models import newslatteremail

def home(request):
    if "subscribe" in request.POST:
        email=newslatteremail()
        email.userEmail=request.POST.get('email')
        email.save()
        messages.info(request,'success subribed')

    if "unsubscribe"  in request.POST:
        newslatteremail.objects.get(userEmail=request.POST.get('email')).delete()   
        messages.info(request,"sorry to see you")

    return render(request,'news.html')