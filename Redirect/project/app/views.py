from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home1(req):
    return redirect("about")

def about(req):
    return redirect("its redirect")

def home2(req):
    return redirect("https://www.startbucks.com/")

def home3(req):
    return redirect("home4")

def home4(req):
    return redirect("https://www.startbucks.com/")
