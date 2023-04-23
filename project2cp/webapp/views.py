from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render,redirect
import os
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, logout
from django.contrib.auth import  login as MyLogin 
from django.contrib import messages
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sessions.backends.db import SessionStore


# Create your views here.

def home (request):
    return  render(request,'webapp/home.html')



def inscrip1(request):
    form1 = Inscription1()
    if request.method == 'POST':
        form1 = Inscription1(request.POST)
        if form1.is_valid():
            request.session['form1_data'] = request.POST
            #form1.save()
            return redirect('/inscription2')
        else:
            print(form1.errors)
            print("Une erreur s'est produite lors de l'enregistrement des données.")

    context = {'form1': form1}
    return render(request, 'webapp/inscrip1.html', context)


def inscrip2(request):
    form2 =Inscription2()
    if request.method == 'POST':
        form2 = Inscription2(request.POST)
        if form2.is_valid():
            #page2= form2.save(commit=False)
            request.session['form2_data'] = form2.cleaned_data
            #form2.save()
            print("Données enregistrées avec succès !")
            return redirect('/inscription3')
        else:
            print(form2.errors)
            print("Une erreur s'est produite lors de l'enregistrement des données.")

    context = {'form2': form2}
    return render(request, 'webapp/inscrip2.html', context)




def inscrip3(request):
    form3 = Inscription3()
    if request.method == 'POST':
        form3 = Inscription3(request.POST)
        if form3.is_valid():
            # Stocker les données dans la session
            request.session['form3_data'] = form3.cleaned_data
            # Créer l'objet final en combinant les données des trois pages de formulaire
            data = {}
            data.update(request.session['form1_data'])
            data.update(request.session['form2_data'])
            data.update(request.session['form3_data'])
            
            data.pop('csrfmiddlewaretoken', None)
            
            nouvel_Doctorant = Doctorant(**data)
            nouvel_Doctorant.nbr_annees_inscription = 1
            #tab_PVs = request.session['form1_data'].get('num_PV')
            #nouvel_Doctorant.tab_PVs.set(tab_PVs)
            nouvel_Doctorant.save()
            # Supprimer les données de session
            del request.session['form1_data']
            del request.session['form2_data']
            del request.session['form3_data']

            return redirect('/inscription1')

    context = {'form3': form3}
    return render(request, 'webapp/inscrip3.html', context)




####################connexion page########################
##########################################################


def login (request):
    context={}
    return  render(request,'webapp/login.html',context)
  


def register (request):
    form=CreateNewUser()
    if request.method=='POST':
        form=CreateNewUser(request.POST)

        if form.is_valid():
          form.save()
          user=form.cleaned_data.get('username')
          messages.success(request, user+'  Created successfully !')
          return redirect('login')
        else:
         messages.info(request,'there is somthing rong:)')
        

    context={'form':form}
    return  render(request,'webapp/register.html',context)



def userLogin (request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
           print("okkkkkkkkkkk")
           MyLogin (request,user)
           print("yeeeeeeeeeeeeeeeees")
           return redirect('/profile/')
        else:
         messages.info(request,'Credentials Error')
         #print(form.errors)
         print("Credentials Error")

    context={}
    return  render(request,'webapp/login.html',context)

  
def userlogout (request):
   logout (request)
   return redirect('login')


##################ikram#################
########################################


def upload_file(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid:
      file = request.FILES['file']
      file_name, file_ext = os.path.splitext(file.name)  # get the filename and extension of the uploaded file
      test = PV.objects.create(numéro=file_name, fichier=file)
      test.save()
      return HttpResponse("The name of uploaded file is " + str(file) + "in PV" + str(test.pk))
  else: 
    form = UploadFileForm()
  return render(request,'webapp/fichier.html', {'form':form})


def add_séminaire(request):
  form = SéminaireForm()
  if request.method == 'POST':
       form = SéminaireForm(request.POST)
       if form.is_valid():
         form.save()
         return redirect('/séminaire')

  return render(request, 'webapp/séminaire.html',  {'form':form})










