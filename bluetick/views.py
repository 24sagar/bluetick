from django.shortcuts import render
from django.shortcuts import redirect

from services.models import Service
from aboutus.models import Aboutus

def index(request):
    return render(request,"index.html")

def about(request):
    aboutusdata = Aboutus.objects.all()
    data = {
        'aboutusdata':aboutusdata
    }
    return render(request,"about.html",data)

def contact(request):
    return render(request,"contact.html")

def services(request):
    servicedata = Service.objects.all()
    data = {
        'servicedata':servicedata
    }
    return render(request,"services.html",data)

