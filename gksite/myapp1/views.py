from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def hai(request):
    return HttpResponse("hai iam again creation my web page can pleasre make sure iam gooding in good way") 

def hai2(request):
    return HttpResponse("hai iam again creation my web page can pleasre make sure iam gooding in good way") 

def hai3(request):
    return HttpResponse("hai iam again creation my web page can pleasre make sure iam gooding in good way") 

def hai4(request):
    return HttpResponse("hai iam again creation my web page can pleasre make sure iam gooding in good way") 

def mydeatils(request):
    name="gopalakrishna"
    my_dict={"name":name,"age":27,"sex":"male","qualificatio":"B.Tech"}
    return render(request,'myapp1temp/auto.html',context=my_dict)