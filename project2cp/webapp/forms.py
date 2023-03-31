from django.forms  import ModelForm 
from .models import   *
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User



class CreateNewUser(UserCreationForm ):
   class Meta:
    model= User
    fields=['username','email','password1','password2']



class Inscription1(ModelForm ):
   tab_PVs = forms.ModelMultipleChoiceField(
        queryset=PV.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
   class Meta:
    model= Doctorant
    fields=['tab_PVs','nom','prénom','date_de_naissance', 'sexe','telephone','email']#photo, 
   


class Inscription2(ModelForm ):
   class Meta:
    model= Doctorant
    fields=['etablissement_origine','option','type_doc','premiere_annee_inscription','date_EFST','laboratoire','titre_these']


class Inscription3(ModelForm ):
   class Meta:
    model= Doctorant
    fields=['directeur','co_directeur','observation']

    
class UploadFileForm(forms.Form):
    file = forms.FileField()


class SéminaireForm(ModelForm):
    class Meta:
        model = Séminaire 
        fields = '__all__'