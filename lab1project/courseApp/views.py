from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse("First response")


def second(request):
    return HttpResponse("Second response")

def third(request):
    return HttpResponse("Third response")