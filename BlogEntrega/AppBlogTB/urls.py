from django.urls import path
from AppBlogTB import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('bienvenida/', views.bienvenida, name ="Bienvenida"),
    path('mi_blog/', views.mi_blog),
    path('inicio/', views.inicio, name ="Inicio"),
    path('autor/', views.autor, name ="Autor"),
    path('comentario/', views.comentario, name="Comentario"),
    path('paper/', views.paper, name="Paper"),
    path('lector/', views.lector, name="Lector"),
    path('more/', views.more, name="More"),
    path('paperform/', views.ingresarPaper, name="Paperform"),
    path('escritorform/', views.ingresarEscritor, name="Escritorform"),
    path('paginaConstruccion/', views.paginaConstruccion, name = "paginaConstruccion"),
]

# Para CRUD sin vistas para Escritor
urlpatterns += [
    path('escritoresLeer/', views.leerEscritores, name = "EscritoresLeer"),
    path('paperLeer/', views.leerPapers, name = "paperLeer"),
    path('eliminarEscritor<escritor_id>/', views.eliminarEscritor, name = "eliminarEscritor"),
    path('editarEscritor/<escritor_id>/', views.editarEscritor, name="editarEscritor")
]

# Para CRUD con vistas basadas en clase para Paper
urlpatterns += [
    path('class-list/', views.PaperListView.as_view(), name="List"),
    path('class-detail/<pk>/', views.PaperDetailWiew.as_view(), name="Detail"),
    path('class-create/', views.PaperCreateView.as_view(), name="Create"),
    path('class-edit/<pk>/', views.PaperUpdateView.as_view(), name="Edit"),
    path('class-delete/<pk>/', views.PaperDeleteView.as_view(), name="Delete"),
]

# Para login, logout, authenticate
urlpatterns += [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='AppBlogTB/logout.html'), name='Logout'),
    path('editarPerfil/', views.editarPerfil, name='EditarPerfil'),
]

