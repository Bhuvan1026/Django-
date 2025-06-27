from django.shortcuts import render,HttpResponse

import wikipedia

def home(request):
    if request.method=='POST':
        search=request.POST['search']
        try:
            result=wikipedia.summary(search,sentences=3)

        except:
            return HttpResponse("wrong input")    
        return render(request,'main/index.html',{'result':result})
    return render(request,'main/index.html')
