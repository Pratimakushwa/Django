from django.shortcuts import render

# Create your views here.
def landingpage(req):
    return render(req,'landingpage.html')

def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def login(req):
    return render(req,'login.html')

def base(req):
    return render(req,'base.html')

