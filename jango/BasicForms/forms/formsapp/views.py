from django.shortcuts import render

# Create your views here.

def get_name(request):
    if request.method=="POST":
        form=NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("thanks/",form)
        else:
            return HttpResponse("Error")
    else:
        form=NameForm()
    return render(request,"formdemo.html",{"form":form})
