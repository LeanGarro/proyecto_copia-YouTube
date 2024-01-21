from django.http import HttpResponse
from django.template import Template, context
from django.shortcuts import render

def saludo(request):
    datos = {"user": "juan", "possword": 123456 }
    return render(request, "index.html", context= datos)

def perfil(request):
    user_name= "juan"
    user_possword= "123456"
    datos= {"user": user_name, "possword": user_possword}
    return render(request, "perfil.html", context= datos)

def user(request):
    ...