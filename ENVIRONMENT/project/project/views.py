from django.http import HttpResponse

def home (req):
    return HttpResponse ("my first django project")