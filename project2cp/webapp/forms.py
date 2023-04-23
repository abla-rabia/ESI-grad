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


class UploadFileForm(forms.Form):
    file = forms.FileField()


class SéminaireForm(ModelForm):
    class Meta:
        model = Séminaire 
        fields = '__all__'





