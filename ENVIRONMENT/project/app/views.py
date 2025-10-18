from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
# static function
# def app(request):
#     html="<h1> this is html<h1/>"
#     return HttpResponse("my first django project",
#        content_type="text/html")            
    
# def app(request):
#     html="<h1> this is html<h1/>"
#     return HttpResponse(html,
#        content_type="text/html")                


# def home1(request,name):
#     return HttpResponse(f'hello{name}')

# # dyanamic function
# def home2(request,pk):
#     return HttpResponse(f'hello{pk}')

# def home3(request,pk):
#     return HttpResponse(f'hello{pk}')

# def home4(request,pk):
#     return HttpResponse(f'hello{pk}')



# def gauri(req):
#     return redirect('prabhat')

# def gauri123(req):
#     return HttpResponse("hello....")

def gauri(req):
    return redirect('/prabhat/')

def gauri123(req):
    return HttpResponse("hello....")

def new123(req):
    return render( req,'home.html')


