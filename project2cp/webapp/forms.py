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
   

class ReinscriptionForm(forms.Form):
    fichier_nom = forms.CharField(label='Numéro du PV', max_length=100)
    doctorant_emails = forms.CharField(label='Emails des doctorants à réinscrire', widget=forms.Textarea)


class ChangementDeTitreForm(forms.Form):
    fichier_nom = forms.CharField(label='Numéro du PV', max_length=100)
    doctorant_email = forms.CharField(label='Email du doctorant',  max_length=100)
    nv_titre = forms.CharField(label='Nouveau titre de thèse',  max_length=100)


class SoutenanceForm(forms.Form):
    fichier_nom = forms.CharField(label='Numéro du PV', max_length=100)
    doctorant_emails = forms.CharField(label='Emails des doctorants qui ont soutenu', widget=forms.Textarea)
    date = forms.DateField(label="Date de soutenance")


class RadiationForm(forms.Form):
    fichier_nom = forms.CharField(label='Numéro du PV', max_length=100)
    doctorant_email = forms.CharField(label='Email du doctorant',  max_length=100)


class AbondantForm(forms.Form):
   fichier_nom = forms.CharField(label='Numéro du PV', max_length=100)
   doctorant_email = forms.CharField(label='Email du doctorant',  max_length=100)
 