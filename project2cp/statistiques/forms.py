from django import forms
from webapp.models import Doctorant

class StatistiquesForm(forms.Form):
    critere1 = forms.ChoiceField(
        # Liste des choix sous forme de tuples (valeur, libellé)
        choices=[('sexe', 'Sexe'),('type_doc', 'Type_doc'),('option', 'Option'),('statut', 'Statut')],
        # Définition des attributs de l'élément HTML utilisé pour afficher le champ
        widget=forms.Select(attrs={'class': 'form-control my-custom-class'})
    )
    critere2 = forms.ChoiceField(choices=[('','None'),('sexe', 'Sexe'),('type_doc', 'Type_doc'),('option', 'Option'),('statut', 'Statut')],initial='',required=False)
    
    date_debut = forms.DateField(label="Date de début",required=False)
    date_fin = forms.DateField(label="Date de fin",required=False)
    def clean(self):
        cleaned_data = super().clean()
        critere1 = cleaned_data.get('critere1')
        critere2 = cleaned_data.get('critere2')
        
        if critere1 == critere2:
            raise forms.ValidationError("Les critères doivent être différents.")

