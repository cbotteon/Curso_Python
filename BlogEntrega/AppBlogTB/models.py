from django.db import models

# Create your models here.
class Blog(models.Model):
    nombre = models.CharField(max_length=40)
    anio = models.IntegerField()

class Lector(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField(unique=True)
    profesion = models.CharField(max_length=30)
    email = models.EmailField()
    
class Escritor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField(unique=True)
    profesion = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre y Apellido: {self.nombre} {self.apellido} - Documento: {self.documento} - Profesión: {self.profesion} - E-Mail: {self.email}"
# este método es para imprimirlo en admin con más escrito o para leer o modificar

class Paper(models.Model):
    titulo = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=30000)
    documento_autor = models.ForeignKey(Escritor, on_delete=models.CASCADE, to_field='documento', default=0)
    anio_publicacion = models.IntegerField()
    palabras_claves = models.CharField(max_length=20)

    def __str__(self):
        return f"Título: {self.titulo} ({self.anio_publicacion}) - Palabras claves: {self.palabras_claves}"

class Comentarios(models.Model):
    titulo_paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    titulo_comentario = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=1200)
    documento_comentarista = models.ForeignKey(Lector, on_delete=models.CASCADE, to_field='documento', default=0)
    anio_publicacion = models.IntegerField()

# Creo la clase Usuario para Login

