from django.shortcuts import render,redirect
import requests

BITLY_ACCESS_TOKEN='c7c3341ed127aed9cafd3d6116be13fac6e8b482'

def index(request):
    return render(request,"index.html")


def index_form(request):
    if request.method=="POST":
        long_url=request.POST.get("long_url")
        shortened_url=shorten_url(long_url)
        return render(request,'new_url.html',{
            'shortened_url':shortened_url
        })
    return redirect('index') 

def shorten_url(long_url):
    url='https://api-ssl.bitly.com/v4/shorten'
    headers={
        'Authorization':f'Bearer {BITLY_ACCESS_TOKEN}',
        'Content-Type':'application/json'
    }
    data={'long_url':long_url}

    response=requests.post(url,headers=headers,json=data)

    if response.status_code==200:
        return response.json()['link']
    else:
        return "Error Shorteningg Url" 