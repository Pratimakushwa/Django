from django.db import models

# Create your models here.
# class Student(models.Model):
#     name=models.CharField(max_length=50)
#     email= models.EmailField()
#     contact=models.CharField(max_length=10)
#     image=models.ImageField(upload_to='image')
#     document=models.FileField(upload_to='file')
#     audio=models.FileField(upload_to='audio')
#     vedio=models.FileField(upload_to='vedio')


class Student(models.Model):
    name=models.CharField(max_length=50)
    email= models.EmailField(null=True)
    contact=models.IntegerField(null=True)
    image=models.ImageField(upload_to='image', null=True)
    document=models.FileField(upload_to='file',null=True)
    audio=models.FileField(upload_to='audio',null=True)
    vedio=models.FileField(upload_to='vedio',null=True)
