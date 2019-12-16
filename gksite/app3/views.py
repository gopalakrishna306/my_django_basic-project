from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def gop (request):
    return HttpResponse("<h1>hai this is GK</h1>")

def vek (request):
    return HttpResponse("hai this is vK")

def rk (request):
    return HttpResponse("hai this is RK")

def mk (request):
    return HttpResponse("hai this is mK")


def template(request):
    return render(request,"app3temp/test.html")

def myimg(request):
    return render(request,"app3temp/pr3.html")


def time(request):
    from datetime import datetime
    d=datetime.now()
    name="gopalakrishna"
    sitename="gk-website"
    dict={"mydate":d,"my_name":name,"my_site":sitename}
    return render(request,'app3temp/time.html',context=dict)
 



