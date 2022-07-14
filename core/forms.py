from cProfile import label
from xml.dom import ValidationErr
from django import forms
from .models import contacto,producto
from django.forms import ValidationError

class contactoForm(forms.ModelForm):


    class Meta:
        model = contacto
        fields ='__all__'
      

class productoForm(forms.ModelForm):




    class Meta:
        model = producto
        fields ='__all__'
