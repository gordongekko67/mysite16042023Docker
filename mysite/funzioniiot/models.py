from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



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

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title