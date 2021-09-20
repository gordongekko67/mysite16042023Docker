from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from .forms import FormContatto
import asyncio
import websockets
import _thread
import time
import paho.mqtt.client as mqtt
import rpyc
import speech_recognition as sr

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet, Titoli2
from .serializers import SnippetSerializer, Titoli2Serializer
from rest_framework import viewsets


class Titoli2View(viewsets.ModelViewSet):
    serializer_class = Titoli2Serializer
    queryset = Titoli2.objects.all()



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
    return render(request, "funzioniiot/websocketclient3.html")

def on_connectmqtt(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

def on_messagemqtt(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def mqttclient(request):
    client = mqtt.Client()
    client.on_connect = on_connectmqtt
    client.on_message = on_messagemqtt

    client.username_pw_set("fkjqkoul","wK0aUWpQWS35")
    client.connect("tailor.cloudmqtt.com", 16434 , 60 )
    client.subscribe("Tutorial2/#", 1)

    client.publish("Tutorial2", "Getting started with MQTT TEST")
    print("prova")
    time.sleep(1)
    while True:
        client.publish("Tutorial2", "Loop publishing")
        client.on_message = on_messagemqtt
        print("publish")
        time.sleep(15)


    client.loop_stop()
    client.disconnect()


def rpgcallpi400(request):
    conn = rpyc.classic.connect("localhost")
    conn.execute("print('Hello from Tutorialspoint')")
 
    conn.execute('import math')
    conn.eval('2*math.pi')

def comandivocali(request):
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

    try:
        print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")
    return HttpResponse("<h1> Fine della prova vocale</h1>")




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




