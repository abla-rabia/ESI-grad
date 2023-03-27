from django.forms import ModelForm
from django import forms
from .models import *


class UploadFileForm(forms.Form):
    file = forms.FileField()


class SéminaireForm(ModelForm):
    class Meta:
        model = Séminaire 
        fields = '__all__'


class EncadrantForm(ModelForm):
    class Meta:
        model = Encadrant
        fields = '__all__'
   