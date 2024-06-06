from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password



User = get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')




    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user



User = get_user_model()

class AddUserForm(UserCreationForm):
    # email = forms.EmailField()
    # first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=30)
    
    group = forms.ModelChoiceField(queryset=Group.objects.all(), widget= forms.Select(attrs={'class': 'form-control2', 'placeholder': 'Group'}),)
    password1 = forms.CharField(
        label=("password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password2'}),
        help_text=(""),
        validators=[validate_password],
        error_messages={
           
        },
        
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password2'}),
        strip=False,
        help_text=(""),
        validators=[validate_password],
        error_messages={
           
        },
    )
    email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        )
    first_name = forms.CharField(
        label='Nom', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom', }),
        )
    last_name = forms.CharField(
        label='Prenom', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
        )
    
    
    
  
    class Meta:
        model = User
        fields = ('email', 'first_name','last_name', 'password1', 'password2', 'group')
       

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        group = self.cleaned_data['group']
        if commit:
            user.save()
        if group == 'admin':
            user.is_staff=True
    
            
        user.groups.add(group)
        user.save()
        return user
    
   





class LoginForm(AuthenticationForm):
    username = forms.EmailField()



class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input-style',
        'placeholder': 'la_rabia@esi.dz',
        'name': 'Votre Email:'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-style',
        'placeholder': '*************************',
        'name': 'Mot De Passe:'
    }))
