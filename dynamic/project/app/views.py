from django.shortcuts import render

# Create your views here.

def landing(request):
    return  render(request,'landing.html')

def select1(request):
    print("hello")
    print(request.method)
    print(request.GET)

    x=request.GET.get('selectoption')
    print(x)
