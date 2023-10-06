from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from AppBlogTB import models
from AppBlogTB.models import Paper
from AppBlogTB.models import Escritor
from AppBlogTB.forms import PaperFormulario
from AppBlogTB.forms import EscritorFormulario


# Create your views here.

def mi_blog(self):
    mi_blog = models.Blog(nombre = "Proyectos", anio = 2023)
    mi_blog.save()
    texto = f"Blog: {mi_blog.nombre}, año: {mi_blog.anio}."
    return HttpResponse(texto)

def escritor(self):
    publicacion = models.Escritor(nombre = "Alejandro", apellido = "Trapé", documento = 17021838, profesion = "Licenciado en Economía", email = "aletrape@gmail.com")
    publicacion.save()
    texto = f"El autor de este paper es {publicacion.nombre} {publicacion.apellido}. DNI: {publicacion.documento}."
    return HttpResponse(texto)

def paper(request):
    return render (request, "AppBlogTB/paper.html")

def comentario(request):
    return render (request, "AppBlogTB/comentario.html")

def autor(request):
    return render (request, "AppBlogTB/autor.html")

def lector(request):
    return render (request, "AppBlogTB/lector.html")

def inicio(request):
    return render (request, "AppBlogTB/inicio.html")

def ingresarPaper(request):
    if request.method == "POST":
        miFormulario = PaperFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            paper = Paper(titulo=informacion["titulo"], documento_autor=informacion["documento_autor"], cuerpo = informacion["cuerpo"], anio_publicacion = informacion["anio_publicacion"], palabras_claves = informacion["palabras_claves"] )
            paper.save()
            return render(request, "AppBlogTB/inicio.html")
    else:
        miFormulario = PaperFormulario()
        return render(request, "AppBlogTB/paperFormulario.html", {"miFormulario": miFormulario})

def ingresarEscritor(request):
    if request.method == "POST":
        miFormulario1 = EscritorFormulario(request.POST) 
        print(miFormulario1)
        if miFormulario1.is_valid():
            informacion = miFormulario1
            escritor = Escritor(nombre=informacion["nombre"], apellido=informacion["apellido"], documento = informacion["documento"], profesion = informacion["profesion"], email = informacion["email"] )
            escritor.save()
            return render(request, "AppBlogTB/inicio.html")
    else:
        miFormulario1 = EscritorFormulario()
        return render(request, "AppBlogTB/escritorFormulario.html", {"miFormulario1": miFormulario1})

def buscarApellidoEscritor(request):
    return render (request, "AppBlogTB/busquedaApellidoEscritor.html")

def buscar(request):
    
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        documento= Escritor.objects.filter(apellido__icontains = apellido)
    
        return render (request, "AppBlogTB/busquedaApellidoEscritor.html", {"documento": documento, "apellido": apellido})

    else: respuesta = "Revisar ingreso de datos"

    return HttpResponse(respuesta)