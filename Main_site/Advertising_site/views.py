from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'main/main.html')


def registration(request):
    return render(request, 'main/registration.html')


def create(request):
    print(request.method)
    print('*' * 150)
    print(request.POST)
    print('*' * 150)
    return redirect('/')



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
