from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.

def get_name(request):
    if request.method=="POST":
        form=NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/",form)
        else:
            return HttpResponse("Error")
    else:
        form=NameForm()
    return render(request,"formdemo.html",{"form":form})

def thanks(request):
    return render(request,'thanks.html')
    
# def first_view(request):
#     return render(request,'first.html')


    


