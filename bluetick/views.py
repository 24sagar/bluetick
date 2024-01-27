from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

from services.models import Service
from aboutus.models import Aboutus
from contact.models import Contact


def index(request):
    return render(request,"index.html")

def about(request):
    aboutusdata = Aboutus.objects.all()
    data = {
        'aboutusdata':aboutusdata
    }
    return render(request,"about.html",data)

def contact(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        # phone = request.POST["phone"]
        message = request.POST["message"]
        obj=Contact(fname=fname,lname=lname,email=email,message=message)
        obj.save()
        return redirect('contact')
    return render(request,"contact.html")

def services(request):
    servicedata = Service.objects.all()
    data = {
        'servicedata':servicedata
    }
    return render(request,"services.html",data)

