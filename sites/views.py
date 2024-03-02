from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def sites(request):
    return HttpResponse("Sites view")



