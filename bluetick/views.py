from django.shortcuts import render
from django.shortcuts import redirect

from services.models import Service

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def services(request):
    servicedata = Service.objects.all()
    data = {
        'servicedata':servicedata
    }
    return render(request,"services.html",data)

