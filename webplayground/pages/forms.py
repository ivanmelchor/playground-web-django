from django import forms
from .models import Page

# Formulario de página "Genérico"
class PageForm(forms.ModelForm):

    # Redefinimos la forma de mostrar el contenido para hacerlo compatible con Bootstrap
    class Meta:
        model = Page
        # Campos a mostrar
        fields = ['title','content','order']
        # Características individuales de cada atributo, esto se mostrará en el formulario y cambiará la forma que se ve
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Orden'}),
        }
        # Elejimos que información se mostrará en la parte de las label 'atributo':'valor a mostrar'
        labels = {
            'title':'', 'order':'',
        }