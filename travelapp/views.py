from django.shortcuts import render
from django.http import HttpResponse
from . models import place,tip

# Create your views here.
def fun(request):
    obj= place.objects.all()
    tips=tip.objects.all()

    return render(request,"index.html",{'results':obj,'tips':tips})

def addition(request):
    num1=(request.POST.get("num1"))
    num2=(request.POST.get("num2"))
    num3=int(num1)+int(num2)
    return render(request,"result.html",{'add':num3})