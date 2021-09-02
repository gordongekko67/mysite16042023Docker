from django import forms
from  django.core.exceptions import ValidationError
#from  django.core import validator



class InputContatto(forms.Form):
   val1 = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))
   val2 = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))
   