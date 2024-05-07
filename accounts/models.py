from django.db import models
import datetime
import os

def filepath(request, filename):
    filename_original = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, filename_original)
    return os.path.join('uploads/', filename)
    
class Member(models.Model):
    name = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=2, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to=filepath,null=True,blank=True)
    

    def __str__(self):
        return self.name
    
  
