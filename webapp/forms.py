from django.forms import ModelForm
from django import forms
from .models import *

class UploadFileForm(forms.Form):

    numéro = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder': 'Numéro du PV'}))
    année = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder': 'Année du PV'}))
    ordre = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control2', 'placeholder': 'Ordre du jour'}))
    file = forms.FileField(
    required=True, 
    label='Fichier', 
    widget=forms.ClearableFileInput(attrs={'class': 'custom-file-upload','placeholder': 'slectionner un fichier'}), 
    )


class SéminaireForm(ModelForm):
    class Meta:
        model = Séminaire 
        fields = '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du séminaire'}),
            'type_seminaire': forms.Select(attrs={'class': 'form-control2'}),
            'résumé': forms.Textarea(attrs={'class': 'form-control2', 'placeholder': 'Résumé du séminaire'}),
        }

class EncadrantForm(ModelForm):
    class Meta:
        model = Encadrant
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prénom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'etablissement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Etablissement'}),
            'laboratoire': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Laboratoire'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Grade'}),
            'interets': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Intérêts'}),
        }


class ReinscriptionForm(forms.Form):
    pv_choice = forms.ModelChoiceField(queryset=PV.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Selectionner un PV", required=True )
    
class ChangementDeTitreForm(forms.Form):
    pv_choice = forms.ModelChoiceField(queryset=PV.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Selectionner un PV", required=True )    
    nv_titre = forms.CharField(label='Nouveau titre de thèse', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control2'}))

class SoutenanceForm(forms.Form):
    pv_choice = forms.ModelChoiceField(queryset=PV.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Selectionner un PV", required=True )    
    date = forms.DateField(
        label="Date de soutenance",
        help_text="Entrer une date ayant le format AAAA-MM-JJ",
        required=True,
        
        widget=forms.DateInput(attrs={'class': 'form-control2', 'placeholder': 'AAAA-MM-JJ','style': 'margin-left: 20px;','type':'date'})
    )


class RadiationForm(forms.Form):
    pv_choice = forms.ModelChoiceField(queryset=PV.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Selectionner un PV", required=True )


 


class Inscription1(ModelForm):
    tab_PVs = forms.ModelMultipleChoiceField(
        queryset=PV.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control3', 'placeholder': 'PV'})
        
    )
    class Meta:
        model = Doctorant
        fields = ['tab_PVs','nom', 'prénom', 'date_de_naissance', 'sexe', 'telephone', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prénom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'date_de_naissance': forms.TextInput(attrs={'class': 'form-control2', 'placeholder': 'Date de naissance', 'type': 'date'}),
            'sexe': forms.Select(attrs={'class': 'form-control2', 'placeholder': 'Sexe'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }



class Inscription2(ModelForm):
    class Meta:
        model = Doctorant
        fields = ['etablissement_origine', 'option', 'type_doc', 'diplome', 'premiere_annee_inscription', 'date_EFST', 'laboratoire', 'titre_these']
        widgets = {
            'etablissement_origine': forms.TextInput(attrs={'class': 'form-control','placeholder':'Etablissement'}),
            'option': forms.Select(attrs={'class': 'form-control2','placeholder':'Option'}),
            'type_doc': forms.Select(attrs={'class': 'form-control2','placeholder':'Type doctorat'}),
            'diplome': forms.Select(attrs={'class': 'form-control2','placeholder':'Diplome'}),
            'premiere_annee_inscription': forms.TextInput(attrs={'class': 'form-control2','placeholder':'Date','type': 'date'}),
            'date_EFST': forms.DateInput(attrs={'class': 'form-control2','placeholder':'Date EFST','type': 'date'}),
            'laboratoire': forms.TextInput(attrs={'class': 'form-control','placeholder':'laboratoire'}),
            'titre_these': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titre these'}),
        }
        


class Inscription3(ModelForm):
    class Meta:
        model = Doctorant
        fields = ['directeur', 'co_directeur', 'observation']
        widgets = {
            'directeur': forms.Select(attrs={'class': 'form-control2', 'placeholder': 'Directeur'}),
            'co_directeur': forms.Select(attrs={'class': 'form-control2', 'placeholder': 'Co-Directeur'}),
            'observation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Observation'})
        }

class RechercheDoctorantForm(forms.Form):
    nom_prénom = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '   Rechercher un doctorant','style': 'font-size: 14px;'}), label=False)
    date_debut = forms.DateField(required=False, widget=forms.DateInput(attrs={ 'placeholder': 'Date début', 'type': 'date','style': 'font-size: 12px;'}),label=True)
    date_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={ 'placeholder': 'Date fin', 'type': 'date','style': 'font-size: 12px;'}))
    sexe = forms.ChoiceField(choices=[('','Sexe'),('Féminin','Féminin'),('Masculin','Masculin')], initial='', required=False, widget=forms.Select(attrs={'class': 'form-select form-select-sm','style': 'font-size: 12px;'}))
    option = forms.ChoiceField(choices=[('','Option'),('SI','SI'),('SIQ','SIQ')], initial='', required=False, widget=forms.Select(attrs={'class': 'form-select form-select-sm','style': 'font-size: 12px;'}))
    type_doc = forms.ChoiceField(choices=[('','Type'),('LMD','LMD'),('Classique','Classique')], initial='', required=False, widget=forms.Select(attrs={'class': 'form-select form-select-sm','style': 'font-size: 12px;'}))
    statut = forms.ChoiceField(choices=[('','Statut'),('Inscrit','Inscrit'),('Soutenu','Soutenu'),('Radié','Radié'),('Différé','Différé')], initial='', required=False, widget=forms.Select(attrs={'class': 'form-select form-select-sm','style': 'font-size: 12px;'}))
from django import forms

from django import forms

class RecherchePVForm(forms.Form):
    année = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Rechercher les PVs d''une année précise',
                'style': 'font-size: 12px;margin-left: 240px;',
                'class': 'form-control'
            }
        ),
        label='Année'
    )

    ordre = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Rechercher les Pvs contenant un ordre précis',
                'style': 'font-size: 12px; margin-left: 240px;',
                'class': 'form-control'
            }
        ),
        label='Ordre'
    )

class RechercheSéminaireForm(forms.Form):
    titre = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '   Rechercher un séminaire selon le titre','style': 'font-size: 14px;'}), label=False)
    type_seminaire = forms.ChoiceField(choices=[('','Type'),('Interne','Interne'),('Externe','Externe')], initial='', required=False, widget=forms.Select(attrs={'class': 'form-select form-select-sm','style': 'font-size: 12px;'}))
    résumé = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '        Résumé','style': 'font-size: 14px;'}), label=False)


class RechercheEncadrantForm(forms.Form):
    nom_prénom = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '   Rechercher un encadrant','style': 'font-size: 14px;'}), label=False)
    etablissement = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'placeholder': '  Etablissement','style': 'font-size: 14px;'}), label='Etablissement:')
    grade = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'placeholder': '  Grade','style': 'font-size: 14px;'}), label='Grade:')
    interets = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'placeholder': '   Interêt','style': 'font-size: 14px;'}), label='Interêts')
    
class DoctorantForm(forms.ModelForm):
    class Meta:
        model = Doctorant
        fields = ['nom', 'prénom', 'date_de_naissance', 'sexe', 'telephone', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control2'}),
            'prénom': forms.TextInput(attrs={'class': 'form-control2'}),
            'date_de_naissance': forms.TextInput(attrs={'class': 'form-control2','type': 'date'}),
            'sexe': forms.Select(attrs={'class': 'form-control2'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control2'},),
            'email': forms.TextInput(attrs={'class': 'form-control2'},),
        }