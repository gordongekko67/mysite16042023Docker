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
import redis
import random

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet, Titoli2
from .serializers import SnippetSerializer, Titoli2Serializer
from rest_framework import viewsets
from django.conf import settings

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


def redis_tutorial(request):
    # connect to redis
    r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)
    
    total_views = r.incr("counter1")
    num_task =  r.lrange("Array1", 0, 1000)
   
    valore = random.randint(0,1) 
   
    if (valore == 0):
         print("push")
         total_task  = r.rpush("Array1", "elemento")
         
    elif (valore == 1):
         print("pop")   
         total_task  = r.rpoplpush("Array1", "elemento")
         

    return render(request, "funzioniiot/test_redis.html", {'total_views': total_views,'total_task':total_task, 'num_task':num_task})
    

def servomotor(request):
    servo = Servo(25)

    try:
	    while True:
        	servo.min()
        	sleep(0.5)
        	servo.mid()
        	sleep(0.5)
        	servo.max()
          
    except KeyboardInterrupt:
	        print("Program stopped")
    return HttpResponse("<h1> Fine test  servomotor +</h1>")


def scrittura_ThingSpeak(request):
    import urllib.request

    msg=str("678")
    msg = msg.replace(' ', "%20")
    msg = msg.replace('\n', "%0A")
    b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=61HO3DFEOHWUHT4I&field1='+msg)

    return HttpResponse("<h1> Fine test  ThingSpeak</h1>")

def scrittura_Aws_Iot_Mqtt_curl(request):
    #os.system("curl --tlsv1.2 --cacert x590.pem --cert 23ae1de8d1-certificate.pem.crt --key 23ae1de8d1-private.pem.key --request POST --data "{ \"message"\: \"Hello, world\" }"  "https://a1ck460w3itrep-ats.iot.eu-central-1.amazonaws.com:8443/topics/test?qos=1" ")
    return HttpResponse("<h1> Fine  scrittura Aws Iot </h1>")


def scrittura_Aws_Iot_Mqtt_python(request):
    # Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    # SPDX-License-Identifier: MIT-0

    import time as t
    import json
    import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

    # Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, MESSAGE, TOPIC, and RANGE
    ENDPOINT = "a1ck460w3itrep-ats.iot.eu-central-1.amazonaws.com"
    CLIENT_ID = "306295914406"
    PATH_TO_CERTIFICATE = "/home/enrico/Documenti/certificati_aws_iot/23ae1de8d1-certificate.pem.crt"
    PATH_TO_PRIVATE_KEY = "/home/enrico/Documenti/certificati_aws_iot/23ae1de8d1-private.pem.key"
    PATH_TO_AMAZON_ROOT_CA_1 = "/home/enrico/Documenti/certificati_aws_iot/x590.pem"
    MESSAGE = "Hello World"
    TOPIC = "test/testing"
    RANGE = 20

    myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
    myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
    myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

    myAWSIoTMQTTClient.connect()
    print('Begin Publish')
    for i in range (RANGE):
        data = "{} [{}]".format(MESSAGE, i+1)
        message = {"message" : data}
        myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
        print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
        t.sleep(0.1)
    print('Publish End')
    myAWSIoTMQTTClient.disconnect()
