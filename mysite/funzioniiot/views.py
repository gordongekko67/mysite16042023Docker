from django.shortcuts import render

# Create your views here.


def homeiot(request):
    return render(request, "funzioniiot/scelta.html")