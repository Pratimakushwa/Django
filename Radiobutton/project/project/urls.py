"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('select2/',views.select2,name='select2'),

    path ('radio/', views.radio,name='radio'),

    path ('', views.form,name='form'),
    path('fromdata/',views.fromdata,name='fromdata'),

    path('select/',views.select,name='select'),
    path('select1/',views.select1,name='select1'),

    path('checkbox/',views.checkbox,name='checkbox'),
    path('select3/',views.select3,name='select3')

    


]

