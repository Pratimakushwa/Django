from django.shortcuts import render
from.models import Student
# Create your views here.
def fromdata(req):
     if req.method=='POST':
          n=req.POST.get('name')
          e=req.POST.get('email')
          c=int(req.POST.get('contact'))
          i=req.FILES.get('image')
          d=req.FILES.get('document')
          a=req.FILES.get('audio')
          v=req.FILES.get('vedio')
          print(a,n,e,i,v,d,c)

          Student.objects.create(
               name=n, email=e, contact=c,
               image=i, audio=a,vedio=v,document=d

          )
          return render(req,'landing.html')
          


def  all_emp(req):
     # print("hello")
     data=Student.objects.all()
     return render(req,'landing.html',{'all_data':data})

def  all_data(req):
     print("hello")


def  radio(request):
    return render(request,'radio.html')

def select2(request):
    print("hello")



    print(request.method)
    print(request.GET)

    x=request.GET.get('gender')
    print(x)

def form(request):
        return render(request,'form.html')

# def fromdata(req):
#     print('hello')
#     print(req.COOKIES)
#     print(req.FILES)
#     print(req.META)
#     print(req.POST)
#     print(req.GET)
#     # print(req.USER)

#     n=req.POST.get('name')
#     print(n)

#     e=req.POST.get('email')
#     print(e)

#     a=req.FILES.get('audio')
#     print(a)

#     v=req.FILES.get('video')
#     print(v)

#     i=req.FILES.get('image')
#     print(i)

def select(request):
     return render(request,'select.html')

def select1(req):
     print('hello')
     


def checkbox(request):
     return render(request,'checkbox.html')

def select3(request):
     print('hello')



