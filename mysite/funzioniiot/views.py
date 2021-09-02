from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from .forms import FormContatto
import asyncio
import websockets
import _thread
import time


from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet, Titoli2
from .serializers import SnippetSerializer

# Create your views here.



def homeiot(request):
    return render(request, "funzioniiot/scelta.html")


def hellocontattaci(request):
    if request.method == 'POST':
        form = FormContatto(request.POST)
        if form.is_valid():
            print("il form e' valido")
            print("NomE ",  form.cleaned_data["nome"])
            print("Cognome ",  form.cleaned_data["cognome"])
            return HttpResponse("<h1> Grazie per averci contattato </h1>")

    else:
        form = FormContatto()
    context = {"form": form}
    return render(request, "funzioniiot/contattaci.html", context)


def http_response(request):
    return HttpResponse("Hello, world. First return from a django application")


def chiamata_request_get(request):
    print("chiamata  request")
    #r = requests.get('https://api.exchangeratesapi.io/latest')
    r = requests.get('https://api.github.com/events')
    r.json()
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    msg = r.json()
    print(msg)
    return HttpResponse(msg, content_type='text/plain')


def chiamata_request_payload(request):
    print("chiamata  request con payload ")
    payload = {'base': 'USD', 'symbols': 'EUR'}
    r = requests.get('https://api.exchangeratesapi.io/latest', params=payload)
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    msg = r.json()
    print(msg)
    return HttpResponse(msg, content_type='text/plain')


def risposta_endpoint(request):
    titoli = Titoli2.objects.all()
    #data1 = {"titoli": list(titoli.values("codtit2", "codbodytit2"))}
    data2 = {"titoli": list(titoli.values())}
    response = JsonResponse(data2)
    print(response)
    return HttpResponse(response, content_type='text/plain')


def websocketclient(request):
    
    return render(request, "funzioniiot/websocketclient.html")
    
def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    _thread.start_new_thread(run, ())




@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



# class in Python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


class Dog:
     
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method 
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

class Student(Person):
  pass

def lanciaclass():
    Rodger = Dog()
 
    # Accessing class attributes
    # and method through objects
    print(Rodger.attr1)
    Rodger.fun()
    d1 = Dog()
    print(p1.name)




