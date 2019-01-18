"""server views"""
from django.shortcuts import render
from django.http import JsonResponse
from random import random as _random


def index(request):
    """the function of index"""
    return render(request, 'index.html')


def random(request):
    """the function of random"""
    return JsonResponse({'random': _random()})
