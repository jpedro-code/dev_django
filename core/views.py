from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request,nome,idade,escola):
    return HttpResponse(f'<h1>Hello {nome} que tem {idade} anos! e estudou na {escola}<h1>')