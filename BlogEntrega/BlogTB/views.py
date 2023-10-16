from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def saludo(request):
	return HttpResponse("Hola somos Julieta Trapé y Claudia Botteon")

def bienvenida(request):
	return HttpResponse("Espero que les guste nuestro blog")

def fecha(request):
	dia = datetime.now()
	texto = f'Hoy es dia: <br> {dia}'
	return HttpResponse(texto)


