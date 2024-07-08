from django.shortcuts import render

# Create your views here.


def joper(request):
    n={"name1":"AVM","name2":"SAI"}
    return render(request,"joper.html",n)

def oper(request):
    d={"fn":"ayirravu","ln":"venkata mohan sai"}
    return render(request,"oper.html",d)
    