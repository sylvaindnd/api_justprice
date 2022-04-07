from pyexpat import model
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *
import random

def index(request):
    objects = [x for x in Object.objects.all() if not x.used]
    
    if(len(objects)==0):
        for obj in Object.objects.all():
            obj.used = False

    obj = random.choice(objects)

    result = {
        'id': obj.id,
        'image': obj.image,
        'name': obj.name,
        'description': obj.description,
        'price': obj.price,
        'price_before': obj.price_before,
        'price_after': obj.price_after
    }

     
    
    return JsonResponse({'status': 'ok', 'object': result})