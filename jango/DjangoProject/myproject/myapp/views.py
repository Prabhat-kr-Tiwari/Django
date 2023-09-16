from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myview(request):
    return HttpResponse("Hello")
def newview(request):
    return HttpResponse("THis is new view")
def newviews(request):
    return render(request,"home.html")

