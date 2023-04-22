from django.forms import ModelForm
from django import forms
from .models import *


class UploadFileForm(forms.Form):
    file = forms.FileField()


class SéminaireForm(ModelForm):
    class Meta:
        model = Séminaire 
        fields = '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'type_seminaire': forms.Select(attrs={'class': 'form-control'}),
            'résumé': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EncadrantForm(ModelForm):
    class Meta:
        model = Encadrant
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prénom': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'},),
            'etablissement': forms.TextInput(attrs={'class': 'form-control'},),
            'laboratoire': forms.TextInput(attrs={'class': 'form-control'},),
            'grade': forms.TextInput(attrs={'class': 'form-control'},),
            'interets': forms.TextInput(attrs={'class': 'form-control'},),
        }
   

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
 


class Inscription1(ModelForm ):
    #num_PV=forms.CharField(label="Numero du PV",max_length=100,required=False)
    class Meta:
      model= Doctorant
      fields=['nom','prénom','date_de_naissance', 'sexe','telephone','email']#photo, 
   


class Inscription2(ModelForm ):
   class Meta:
    model= Doctorant
    fields=['etablissement_origine','option','type_doc','diplome','premiere_annee_inscription','date_EFST','laboratoire','titre_these']


class Inscription3(ModelForm ):
   class Meta:
    model= Doctorant
    fields=['directeur','co_directeur','observation']