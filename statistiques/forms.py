from django import forms
from webapp.models import Doctorant

class StatistiquesForm(forms.Form):
    critere1 = forms.ChoiceField(
        choices=[('sexe', 'Sexe'),('type_doc', 'Type_doc'),('option', 'Option'),('statut', 'Statut')],
        widget=forms.Select(attrs={'class': 'form-control2'}),
                error_messages={'required': ''}

    )
    critere2 = forms.ChoiceField(
        choices=[('','None'),('sexe', 'Sexe'),('type_doc', 'Type_doc'),('option', 'Option'),('statut', 'Statut')],
        initial='',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control2'}),
    )
    date_debut = forms.DateField(
        label="Date de début",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder': 'Date de début','type': 'date'}),
    )
    date_fin = forms.DateField(
        label="Date de fin",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control2', 'placeholder': 'Date de fin','type': 'date'}),
    )
    def clean(self):
        cleaned_data = super().clean()
        critere1 = cleaned_data.get('critere1')
        critere2 = cleaned_data.get('critere2')
        
        if critere1 == critere2:
            raise forms.ValidationError("")

