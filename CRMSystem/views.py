from django.http.response import HttpResponseNotFound
from django.shortcuts import render

def main_page(request):
    return render(request, 'base.html')

def PageNotFound(request, exception, *args, **kwargs):
    return HttpResponseNotFound('Страница не найдна')