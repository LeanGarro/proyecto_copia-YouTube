from django.http import HttpResponse
from django.template import Template, context

def saludo(request):
    index_html = open("../index.html")
    return HttpResponse(index_html)