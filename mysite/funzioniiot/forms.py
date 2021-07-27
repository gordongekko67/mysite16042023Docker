from django import forms
from  django.core.exceptions import ValidationError
#from  django.core import validator
from  .models  import Titoli2

from django.contrib.auth.models import  User


class FormContatto(forms.Form):
   nome = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
   cognome = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
   email   =  forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
   contenuto = forms.CharField(widget= forms.Textarea(attrs={"placeholder":"Area Testuale scrivi pure", "class":"form-control"}))
