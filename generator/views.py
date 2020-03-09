
from django.shortcuts import render
from django.http import HttpResponse
import random

def method_name(request):
    return render(request, 'generator/home.html')

def about_name(request):
    return render(request, 'generator/about.html')

def password_name(request):

    charecter=list('abcdefghijkklmnopqrstuvwxyz')

    lengths=int(request.GET.get('length', 12))
    paswdkey=''

    if request.GET.get('uppercase'):
        charecter.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        charecter.extend(list('1234567890'))
    if request.GET.get('special'):
        charecter.extend(list('!@#$%^&*()'))

    for i in range(lengths):
        paswdkey=paswdkey+random.choice(charecter)
    return render(request, 'generator/password.html', {'passwords':paswdkey})

