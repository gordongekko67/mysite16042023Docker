from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Titoli2(models.Model):
    codtit2 = models.CharField(max_length=250)
    codslugtit2 = models.SlugField(max_length=250,unique_for_date='codcreatedtit2')
    codauthortit2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_titoli2')                  
    codisintit2= models.CharField(max_length=250) 
    codbodytit2 = models.TextField()
    codpublishtit2= models.DateTimeField(default=timezone.now)
    codcreatedtit2 = models.DateTimeField(auto_now_add=True)
    codupdatedtit2 = models.DateTimeField(auto_now=True)
    codmintit2 = models.FloatField()
    codmaxtit2 = models.FloatField()
   
    def __str__(self):
        return self.codtit2
