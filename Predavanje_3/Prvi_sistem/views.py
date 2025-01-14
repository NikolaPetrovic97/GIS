from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Prvi_sistem.models import Mapa

def index(request):
    return HttpResponse("Prva stranica")

def mape(request):
    return HttpResponse(JsonResponse(list(Mapa.objects.values()), safe=False), content_type="application/json"))

@csrf exempt
def dodaj_mapu(request):
    try:
        data=json.loads(request.body.strip())
        Mapa.objects.create(TopLlat=data['TopLlat'], TopLlat=data['TopLlat'], )
        print(data)
    except:
        
