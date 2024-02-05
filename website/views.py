from django.shortcuts import render, redirect


# Create your views here.
def base(request):
        return render(request,"base.html")

def index(request):
        return render(request,"index.html")

def contact_us(request):
        return render(request,"contact.html")

def about(request):
        return render(request,"about.html")

def service(request):
        return render(request,"service.html")







