from django.shortcuts import render

# Create your views here.

def printNames(request):
    names={"name1":"AVM","name2":"SAI"}
    return render(request,"printNames.html",context=names)


