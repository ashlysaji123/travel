from django.shortcuts import render
from . models import Places,Peoples

def index(request):
    obj=Places.objects.all()
    ob=Peoples.objects.all()
    return render(request,"index.html",{'result':obj,'results':ob})
