from django.forms import ModelForm
from django import forms
from .models import *

"""
class DoctorantForm(ModelForm):
    class Meta:
        model = Doctorant  
        fields = ['nom' , 'prénom']



"""

class UploadFileForm(forms.Form):
    file = forms.FileField()


class SéminaireForm(ModelForm):
    class Meta:
        model = Séminaire 
        fields = '__all__'