from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "polls/base.html", context)

def indextext(request):
    return HttpResponse("Hello, world. First return from a django application")
