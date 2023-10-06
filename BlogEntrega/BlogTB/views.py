from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from datetime import datetime

def saludo(request):
	return HttpResponse("Hola somos Julieta Trapé y Claudia Botteon")

def bienvenida(request):
	return HttpResponse("Espero que les guste nuestro blog")

def fecha(request):
	dia = datetime.now()
	texto = f'Hoy es dia: <br> {dia}'
	return HttpResponse(texto)

def usando_loader(request):
    nombre = "Juli"
    apellido = "Trapé"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }
    plantilla = loader.get_template('Template3.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

# Uso de louder para dar el path mas directo. Evita codigo. Ojo que tuve que poner en setting la ruta con
# doble barra invertida.

