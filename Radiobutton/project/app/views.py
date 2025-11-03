from django.shortcuts import render

# Create your views here.


def  base(request):
    return render(request,'base.html')

def select2(request):
    print("hello")



    print(request.method)
    print(request.GET)

    x=request.GET.get('gender')
    print(x)

def form(request):
        return render(request,'form.html')


def fromdata(req):
    print('hello')
    print(req.COOKIES)
    print(req.FILES)
    print(req.META)
    print(req.POST)
    print(req.GET)
    # print(req.USER)

    n=req.POST.get('name')
    print(n)

    e=req.POST.get('email')
    print(e)

    a=req.FILE.get('audio')
    print(a)

    v=req.FILE.get('video')
    print(v)

    i=req.FILE.get('image')
    print(i)