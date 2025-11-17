from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=15, null=True, blank=True)

    details = models.TextField(null=True, blank=True)

    gender = models.CharField(max_length=10, null=True, blank=True)

    qualification = models.CharField(max_length=100, null=True, blank=True)

    education = models.CharField(max_length=20, null=True, blank=True)

    profile_pic= models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    document = models.FileField(upload_to="documents/", null=True, blank=True)
    audio = models.FileField(upload_to="audio_files/", null=True, blank=True)
    video = models.FileField(upload_to="video_files/", null=True, blank=True)
    password=models.CharField(max_length=50,null=True)
    confirmpassword = models.CharField(max_length=50,null=True)   

    def __str__(self):
        return self.name

