from django.urls import path
from AppBlogTB import views

urlpatterns = [
    path('mi_blog/', views.mi_blog),
    path('escritor/', views.escritor, name ="Escritor"),
    path('inicio/', views.inicio, name ="Inicio"),
    path('autor/', views.autor, name ="Autor"),
    path('comentario/', views.comentario, name="Comentario"),
    path('paper/', views.paper, name="Paper"),
    path('lector/', views.lector, name="Lector"),
    path('paperform/', views.ingresarPaper, name="Paperform"),
    path('escritorform/', views.ingresarEscritor, name="Escritorform"),
    path('busquedaescritor/', views.buscarApellidoEscritor, name = "BusquedaEscritor"),
    path('buscar/', views.buscar, name = "Buscar"),
]