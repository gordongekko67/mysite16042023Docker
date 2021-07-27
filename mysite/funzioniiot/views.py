from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import requests
from funzioniiot.models import Titoli2
from .forms import FormContatto

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
"""
@api_view(['GET'])
def cliente_collection(request):
    cli = Cliente.objects.all()
    serializer = ClienteSerializer(cli, many=True)
    print(serializer.data)
    content = JSONRenderer().render(serializer.data)
    print(content)
    #

    
    
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)

    serializer = ClienteSerializer(data=data)
    #serializer.is_valid()
    # True
    serializer.validated_data
    # OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
    serializer.save()

    return Response(serializer.data)


def redis_tutorial(request):
    r = redis.Redis()
    r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    r.get("Bahamas")
    today = datetime.date.today()
    visitors = {"dan", "jon", "alex"}
    stoday = today.isoformat()  # Python 3.7+, or use str(today)
    r.sadd(stoday, *visitors)  # sadd: set-add
    r.smembers(stoday)
    a = r.scard(today.isoformat())
    r.set('count',1)
    r.incr('count')

   """