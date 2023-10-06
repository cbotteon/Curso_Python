from django.contrib import admin
from .models import Paper, Escritor, Comentarios, Lector

# Register sus modelos here
 
admin.site.register(Paper)
admin.site.register(Escritor)
admin.site.register(Comentarios)
admin.site.register(Lector)