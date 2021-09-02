from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from .forms import InputContatto


def index(request):
    if request.method == 'POST':
        form = InputContatto(request.POST)
        if form.is_valid():
            print("il form e' valido")
            print("Valore 1 ",  form.cleaned_data["val1"])
            print("Valore 2 ",  form.cleaned_data["val2"])
            v1= form.cleaned_data["val1"]
            v2= form.cleaned_data["val2"]
            percentuale = v1/v2*100
            return HttpResponse("<div>Hello {{percentuale}}</div>")
         

    else:
        form = InputContatto()
    context = {"form": form}
    
    return render(request, "utilitaazioni/index.html", context)

    