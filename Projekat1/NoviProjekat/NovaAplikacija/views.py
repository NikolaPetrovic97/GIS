from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Nova Aplikacija") 

def mape(request):
    return HttpResponse(JsonResponse(list(Mapa.objects.values()), safe=False), content_type="application/json")

@csrf_exempt
def addMap(request):
    try:
        data = json.loads(request.body.strip())
        Mapa.objects.create(TopLlat=data['TopLlat'], TopLlon=data['TopLlon'], BotRlat=data['BotRlat'], BotRlon=data['BotRlon'], imgUrl=data['imgUrl'])
    except:
        return HttpResponse(JsonResponse({'status':'not ok'}, safe=False), content_type="application/json")
    return HttpResponse(JsonResponse({'status':'ok'}, safe=False), content_type="application/json")

@csrf_exempt
def addObjekat(request):
    try:
        data = json.loads(request.body.strip())
        Objekat.objects.create(
            TopLlat=data['TopLlat'],
            TopLlon=data['TopLlon'],
            BotRlat=data['BotRlat'],
            BotRlon=data['BotRlon'],
            mapa_id=data['mapaID'])
    except Exception as err:
        return HttpResponse(JsonResponse({'status':'not ok'}, safe=False), content_type="application/json")
    return HttpResponse(JsonResponse({'status':'ok'}, safe=False), content_type="application/json")

def objekti_mapa(request, mapa_id):
    lista = []
    for i in Obejkat.objects.filter(mapa=mapa_id):
        lista.append(i.as_json())
    return HttpResponse(JsonResponse(lista, safe=False), content_type="applicati
