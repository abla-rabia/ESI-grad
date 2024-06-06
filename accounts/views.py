
from django.shortcuts import render, redirect
from .forms import RegistrationForm,AddUserForm
from django.contrib.auth import authenticate,logout
from .forms import *
from django.contrib.auth import login as auth_login
from webapp.urls import *
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Redirect to success page or homepage
            return redirect('welcome')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})





def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_popup')
    else:
        form = AddUserForm()
    return render(request, 'accounts/add_user.html', {'form': form})



def My_login(request):
    if request.user.is_authenticated:
        return redirect('Acceuil')
    else:
        if request.method == 'POST':
            form = CustomLoginForm(request=request, data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    auth_login(request, user)
                    # Redirect to success page or homepage
                    # return redirect('webapp/Acceuil.html')
                    return redirect('Acceuil')
                    #return redirect(reverse_lazy('webapp:Acceuil'))
                else:
                    form.add_error(None, 'Invalid email or password.')
        else:
            form = CustomLoginForm()
        return render(request, 'accounts/login.html', {'form': form})



def welcome(request):
    return render(request, 'accounts/welcome.html')
def a_propos(request):
    return render(request, 'accounts/A_propos.html')
def contact(request):
    return render(request, 'accounts/contact.html')
def userlogout (request):
   logout (request)
   return redirect('welcome')



def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    paginator = Paginator(users, 8) # Paginer les résultats par 10 doctorants
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'accounts/listuser.html', {'users': users,'page_obj':page_obj})

