from django import forms

class PaperFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=30000)
    documento_autor = forms.IntegerField()
    anio_publicacion = forms.IntegerField()
    palabras_claves = forms.CharField(max_length=20)

