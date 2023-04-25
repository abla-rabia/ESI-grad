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
    pv_choice = forms.ModelChoiceField(queryset=PV.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Selectionner un PV", required=True )
    
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
 


class Inscription1(ModelForm):
    class Meta:
        model = Doctorant
        fields = ['nom', 'prénom', 'date_de_naissance', 'sexe', 'telephone', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prénom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'date_de_naissance': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de naissance'}),
            'sexe': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sexe'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }



class Inscription2(ModelForm):
    class Meta:
        model = Doctorant
        fields = ['etablissement_origine', 'option', 'type_doc', 'diplome', 'premiere_annee_inscription', 'date_EFST', 'laboratoire', 'titre_these']
        widgets = {
            'etablissement_origine': forms.TextInput(attrs={'class': 'form-control','placeholder':'Etablissement'}),
            'option': forms.Select(attrs={'class': 'form-control','placeholder':'Option'}),
            'type_doc': forms.Select(attrs={'class': 'form-control','placeholder':'Type doctorat'}),
            'diplome': forms.Select(attrs={'class': 'form-control','placeholder':'Diplome'}),
            'premiere_annee_inscription': forms.TextInput(attrs={'class': 'form-control','placeholder':'Date'}),
            'date_EFST': forms.DateInput(attrs={'class': 'form-control','placeholder':'Date EFST'}),
            'laboratoire': forms.TextInput(attrs={'class': 'form-control','placeholder':'laboratoire'}),
            'titre_these': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titre these'}),
        }



class Inscription3(ModelForm):
    class Meta:
        model = Doctorant
        fields = ['directeur', 'co_directeur', 'observation']
        widgets = {
            'directeur': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Directeur'}),
            'co_directeur': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Co-Directeur'}),
            'observation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Observation'})
        }

class RechercheDoctorantForm(forms.Form):
    nom_prénom = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '   Rechercher un doctorant','style': 'font-size: 14px;'}), label=False)
    date_debut = forms.DateField(required=False, widget=forms.DateInput(attrs={ 'placeholder': 'Date début', 'type': 'date','style': 'font-size: 12px;'}),label=True)
    date_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={ 'placeholder': 'Date fin', 'type': 'date','style': 'font-size: 12px;'}))
    sexe = forms.ChoiceField(choices=[('','Sexe'),('F','F'),('M','M')], initial='', required=False, widget=forms.Select(attrs={'class': 'form-select form-select-sm','style': 'font-size: 12px;'}))
    option = forms.ChoiceField(choices=[('','Option'),('SI','SI'),('SIQ','SIQ')], initial='', required=False, widget=forms.Select(attrs={'class': 'form-select form-select-sm','style': 'font-size: 12px;'}))
    type_doc = forms.ChoiceField(choices=[('','Type'),('LMD','LMD'),('Classique','Classique')], initial='', required=False, widget=forms.Select(attrs={'class': 'form-select form-select-sm','style': 'font-size: 12px;'}))
    statut = forms.ChoiceField(choices=[('','Statut'),('Inscrit','Inscrit'),('Soutenu','Soutenu'),('Abandon','Abandon')], initial='', required=False, widget=forms.Select(attrs={'class': 'form-select form-select-sm','style': 'font-size: 12px;'}))
