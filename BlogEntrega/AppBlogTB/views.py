from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import Template, Context
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppBlogTB import models
from AppBlogTB.models import Paper
from AppBlogTB.models import Escritor
from AppBlogTB.forms import PaperFormulario, EscritorFormulario, BuscaEscritorForm, UserRegisterForm, UserEditForm


# Create your views here.

def bienvenida(request):
    return render (request, "AppBlogTB/bienvenida.html")

def mi_blog(self):
    mi_blog = models.Blog(nombre = "Trabajos de Economía", anio = 2023)
    mi_blog.save()
    texto = f"Blog: {mi_blog.nombre} - Creado en el año: {mi_blog.anio}."
    return HttpResponse(texto)

def escritor(self):
    publicacion = models.Escritor(nombre = "Alejandro", apellido = "Trapé", documento = 17021838, profesion = "Licenciado en Economía", email = "aletrape@gmail.com")
    publicacion.save()
    texto = f"El autor de este paper es {publicacion.nombre} {publicacion.apellido}. DNI: {publicacion.documento}."
    return HttpResponse(texto)

@login_required  
def paper(request):
    return render (request, "AppBlogTB/paper.html")

@login_required  
def comentario(request):
    return render (request, "AppBlogTB/comentario.html")

def autor(request):
    return render (request, "AppBlogTB/autor.html")

def lector(request):
    return render (request, "AppBlogTB/lector.html")

def more(request):
    return render (request, "AppBlogTB/more.html")

def inicio(request):
    return render (request, "AppBlogTB/inicio.html")

def paginaConstruccion(request):
    return render (request, "AppBlogTB/paginaConstruccion.html")

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
            informacion = miFormulario1.cleaned_data
            escritor = Escritor(nombre=informacion["nombre"], apellido=informacion["apellido"], documento = informacion["documento"], profesion = informacion["profesion"], email = informacion["email"] )
            escritor.save()
            return render(request, "AppBlogTB/inicio.html")
    else:
        miFormulario1 = EscritorFormulario()
        return render(request, "AppBlogTB/escritorFormulario.html", {"miFormulario1": miFormulario1})


# Para CRUD sin vistas para Escritor

def leerEscritores(request):
    escritores = Escritor.objects.all() #trae todos los escritores
    contexto= {"escritores":escritores} 
    return render(request, "AppBlogTB/escritoresLeer.html",contexto)

def leerPapers(request):
    trabajos = Paper.objects.all() #trae todos los trabajos
    contexto= {"trabajos":trabajos} 
    return render(request, "AppBlogTB/paperLeer.html",contexto)

def eliminarEscritor(request, escritor_id):
    escritor = Escritor.objects.get(id=escritor_id)
    escritor.delete()
    escritores = Escritor.objects.all()  # trae todos los profesores
    contexto = {"escritores":escritores}
    return render(request, "AppBlogTB/escritoresLeer.html", contexto)
    # El id no se pone en los modelos, pero django lo crea. Cuando se borra conviene hacerlo por id

def editarEscritor(request, escritor_id):
    escritor = Escritor.objects.get(id=escritor_id)
    if request.method == "POST":
        miFormulario1 = EscritorFormulario(request.POST) 
        print(miFormulario1)
        if miFormulario1.is_valid():
            informacion = miFormulario1.cleaned_data
            escritor.nombre = informacion["nombre"]
            escritor.apellido=informacion["apellido"]
            escritor.documento = informacion["documento"]
            escritor.profesion = informacion["profesion"]
            escritor.email = informacion["email"]
            escritor.save()
            return render(request, "AppBlogTB/inicio.html")
    else:
        miFormulario1 = EscritorFormulario(initial= {
            'nombre': escritor.nombre,
            'apellido': escritor.apellido,
            'documento': escritor.documento,
            'profesion': escritor.profesion,
            'email': escritor.email
            } )
        return render(request, "AppBlogTB/escritorFormulario.html", {"miFormulario1": miFormulario1})


# Para CRUD con vistas basadas en clase para Paper

class PaperListView(ListView):
    model = Paper
    template_name = "AppBlogTB/paperLista.html"

class PaperDetailWiew(DetailView):
    model = Paper
    #success_url = reverse_lazy("List")
    template_name = "AppBlogTB/paperDetail.html"
    #fields = ["titulo", "anio_publicacion"]

class PaperCreateView(CreateView):
    model = Paper
    template_name = "AppBlogTB/paperCreate.html"
    success_url = reverse_lazy("List")
    fields = ["titulo", "anio_publicacion", 'documento_autor','palabras_claves']

class PaperUpdateView(UpdateView):
    model = Paper
    template_name = "AppBlogTB/paperEdit.html"
    success_url = reverse_lazy("List")
    fields = ['titulo', 'cuerpo', 'anio_publicacion', 'palabras_claves']

class PaperDeleteView(DeleteView):
    model = Paper
    success_url = reverse_lazy("List")
    template_name = "AppBlogTB/paperConfirmDelete.html"

# Para login, registro, logout ...

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        print(form) 
        if form.is_valid():
            usuario = form.cleaned_data.get ("username")
            contrasenia = form.cleaned_data.get ("password")
            user = authenticate (username = usuario, password = contrasenia)
            if user is not None:
                login(request,user)
                return render(request, "AppBlogTB/inicio.html", {'mensaje': f"Bienvenido {usuario}"})
            else:
                form = AuthenticationForm()
                return render(request, "AppBlogTB/login.html", {'mensaje': "Los datos ingresados son incorrectos", "form": form})
        else:
            return render(request, "AppBlogTB/inicio.html", {'mensaje': "El formulario es incorrecto"})
    form = AuthenticationForm()
    return render(request, "AppBlogTB/login.html", {"form": form})

# Está heredando de UserCreateForm (con lo que se hace en forms.py)
def register(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                usuario = form.cleaned_data['username']
                form.save()
            return render(request,"AppBlogTB/inicio.html" , {"mensaje":"Usuario Creado!!! Bienvenido"})
      else:
            form = UserRegisterForm()       
            
      return render(request,"AppBlogTB/register.html" ,  {"form":form})

# Vista de editar el perfil (importante: para editar un perfir se requiere estar logueado, ya que le
# impuse esa condicion)

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, "AppBlogTB/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "AppBlogTB/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})



