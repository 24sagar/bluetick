from django.db import models

class Contact(models.Model):
     fname = models.CharField(max_length=50)
     lname = models.CharField(max_length=50)
     email = models.EmailField(max_length=254)
     message = models.TextField()

# Create your models here.
