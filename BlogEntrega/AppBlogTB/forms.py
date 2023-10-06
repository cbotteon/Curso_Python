from django import forms

class EscritorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    documento = forms.IntegerField()
    profesion = forms.CharField()
    email = forms.EmailField()

class PaperFormulario(forms.Form):
    titulo = forms.CharField()
    cuerpo = forms.CharField()
    documento_autor = forms.IntegerField()
    anio_publicacion = forms.IntegerField()
    palabras_claves = forms.CharField()

    # Ponemos los campos que queramos