from django.db import models

class Aboutus(models.Model):
    aboutus_img = models.FileField(upload_to="images/", max_length=250,null=True,default=None)
    aboutus_dec = models.TextField()
    aboutus_title = models.CharField(max_length=50)
    

# Create your models here.


