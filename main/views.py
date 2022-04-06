from turtle import ht
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def index(request):
    return JsonResponse({'status':'ok'})
