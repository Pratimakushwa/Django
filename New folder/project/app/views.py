from django.shortcuts import render,redirect
from .models import Registration
from django.urls import reverse
from urllib.parse import urlencode

def register(req):
    return render(req ,'register.html') 
def login(req):
     return render(req ,'login.html')

def logindata(req):
    if req.method=='POST':
        print(req.POST)
        le = req.POST.get('email')
        lp = req.POST.get('password')
        print(le,lp)
        user=Registration.objects.filter(email=le)
        if user:
          userdata=Registration.objects.get(email=le)
          name=userdata.name
          email=userdata.email
          contact=userdata.contact
          details=userdata.details
          gender=userdata.gender
          audio=userdata.audio
          video=userdata.video
          profile_pic=userdata.profile_pic
          qualification=userdata.qualification
          education=userdata.education
          password=userdata.password
          confirmpassword=userdata.confirmpassword
          print(name,email,contact, details, education,profile_pic,video,audio,qualification,password,confirmpassword,gender)
          if password==lp:
            data={'name':name,'email':email,'contact':contact,'details':details,'gender':gender,'qualification':qualification,'education':education,'profile_pic':profile_pic,'audio':audio,'video':video,'password':password}
            base_url=reverse('dashboard')
            data=urlencode({'name':name,'email':email,'contact':contact,'details':details,'gender':gender,'qualification':qualification,'education':education,'profile_pic':profile_pic,'audio':audio,'video':video,'password':password})
            url=f'{base_url}?{data}'
            return redirect(url )
          else:
            msg="Incorrect Password"
            return render(req,'login.html',{'msg':msg,'email':le})
              
            #   return  render (req, "dashboard.html",data)
       
              
    else:
            msg="email id not register"
            return render(req ,'form.html',{'msg': msg})



def landing(req):
     return render(req , 'landing.html') 
def base(req): 
    return render(req , 'base.html')

def form(req): 
    return render(req , 'form.html')

def registerdata(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        d = request.POST.get('details')
        g = request.POST.get('gender')
        q = request.POST.get('qualification')
        he = request.POST.get('education')
        V = request.FILES.get('video')
        A = request.FILES.get('audio')
        P = request.FILES.get('profile_pic')
        D = request.FILES.get('document')
        p= request.POST.get('password')
        C= request.POST.get('confirmpassword')

        
        user = Registration.objects.filter(email=e)  
        # .first()

        if user:
            msg="email already exit"
            print("Hello")
            return render(request, 'form.html', {'x': 'User already exists'})
        else:
            if p==C:
                Registration.objects.create(
                name=n,
                email=e,
                contact=c,
                details=d,
                gender=g,
                qualification=q,
                education=he,
                video=V,
                audio=A,
                profile_pic=P,
                document=D,
                password=p,
                confirmpassword=C


                )
                return render(request, 'login.html', {'y': 'Registration done'})
            else:
                msg='password and confirm password not mached'
                data={
                'name':n,
                'email':e,
                'contact':c,
                'details':d,
                'gender':g,
                'qualification':q,
                'education':he,
                'video':V,
                'audio':A,
                'profile_pic':P,
                'document':D,
               

                }
                return render(request, 'form.html' ,{'pmsg' :msg,'data':data})
            

        #  Registration.objects.create(
        #         name=n,
        #         email=e,
        #         contact=c,
        #         details=d,
        #         gender=g,
        #         qualification=q,
        #         education=he,
        #         video=V,
        #         audio=A,
        #         profile_pic=P,
        #         document=D,
        #         # password=p,
        #         # confirmpassword=C

        #     )
           
        #     return render(request, 'login.html', {'y': 'Registration Successful'})

    # return render(request, 'register.html')


def dashboard(req):
    print(req.GET)
    name=req.GET.get('name')
    contact=req.GET.get('contact')
    details=req.GET.get('details')
    gender=req.GET.get('gender')
    qualification=req.GET.get('qualification')
    education=req.GET.get('education')  
    profile_pic=req.GET.get('profile_pic')
    audio=req.GET.get('audio')
    video=req.GET.get('video')
    document=req.GET.get('document')
    password=req.GET.get('password')
    email=req.GET.get('email')
    
    print(email,password)
    if email and password:
      name=name
      email=email
      contact=contact
      details=details
      gender=gender
      qualification=qualification
      education=education
      profile_pic=profile_pic
      audio=audio
      video=video
      document=document
      password=password
      data={'name':name,'email':email,'contact':contact,'details':details,'gender':gender,'qualification':qualification,'education':education,'profile_pic':profile_pic,'audio':audio,'video':video,'document':document,'password':password}
      return render (req,'dashboard.html',data)
    else:
      return render (req,'login.html')