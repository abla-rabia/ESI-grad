from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.shortcuts import render,redirect
import os

# Create your views here.



def inscrip0(request):
    return render(request, 'webapp/inscription0.html')

def Acceuil(request):
    return render(request, 'webapp/acceuil.html')

def m_a_j(request):
    return render(request, 'webapp/miseajours.html')



def user_list(request):
    users = User.objects.all()
    return render(request, 'webapp/listuser.html', {'users': users})

def doctorant_list(request):
    doctorants = Doctorant.objects.all()
    context = {
        'doctorants': doctorants
    }
    return render(request, 'webapp/listdoc.html', context)
















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


def add_encadrant(request):
  form = EncadrantForm()
  if request.method == 'POST':
       form = EncadrantForm(request.POST)
       if form.is_valid():
         form.save()
         return redirect('/encadrant')

  return render(request, 'webapp/encadrant.html',  {'form':form})


def reinscription(request):
    if request.method == 'POST':
        form = ReinscriptionForm(request.POST)
        if form.is_valid():
            fichier_nom = form.cleaned_data['fichier_nom']
            fichier = PV.objects.get(numéro=fichier_nom)
            doctorant_emails = form.cleaned_data['doctorant_emails'].split()
            for email in doctorant_emails:
                try:
                    doctorant = Doctorant.objects.get(email=email)
                    doctorant.nbr_annees_inscription += 1
                    doctorant.tab_PVs.add(fichier)
                    doctorant.save()
                except ObjectDoesNotExist:
                    # Do something if the doctorant does not exist
                    pass
            return redirect('/reinscription')
    else:
        form = ReinscriptionForm()
    return render(request, 'webapp/reinscription.html', {'form': form})


def changement_titre(request):
  if request.method == 'POST':
        form = ChangementDeTitreForm(request.POST)
        if form.is_valid():
            fichier_nom = form.cleaned_data['fichier_nom']
            fichier = PV.objects.get(numéro=fichier_nom)
            nv_titre = form.cleaned_data['nv_titre']
            doctorant_email = form.cleaned_data['doctorant_email']
            try:
                    doctorant = Doctorant.objects.get(email=doctorant_email)
                    doctorant.pv_changement_titre = fichier
                    doctorant.nv_titre = nv_titre
                    doctorant.save()
            except ObjectDoesNotExist:
                    # Do something if the doctorant does not exist
                pass
            return redirect('/changementtitre')
  else:
    form = ChangementDeTitreForm()
  return render(request, 'webapp/changementtitre.html', {'form': form})



def soutenance(request):
  if request.method == 'POST':
        form = SoutenanceForm(request.POST)
        if form.is_valid():
            fichier_nom = form.cleaned_data['fichier_nom']
            fichier = PV.objects.get(numéro=fichier_nom)
            date = form.cleaned_data['date']
            doctorant_emails = form.cleaned_data['doctorant_emails'].split()
            for email in doctorant_emails:
                try:
                    doctorant = Doctorant.objects.get(email=email)
                    doctorant.statut = "A soutenue"
                    doctorant.a_soutenue = fichier
                    doctorant.date_soutenance = date
                    doctorant.save()
                except ObjectDoesNotExist:
                    # Do something if the doctorant does not exist
                    pass
            return redirect('/soutenance')
  else:
        form = SoutenanceForm()
  return render(request, 'webapp/soutenance.html', {'form': form})



def radiation(request):
  if request.method == 'POST':
        form = RadiationForm(request.POST)
        if form.is_valid():
            fichier_nom = form.cleaned_data['fichier_nom']
            fichier = PV.objects.get(numéro=fichier_nom)
            doctorant_email = form.cleaned_data['doctorant_email']
            try:
                    doctorant = Doctorant.objects.get(email=doctorant_email)
                    doctorant.radié = fichier
                    doctorant.statut = "Radié"
                    doctorant.save()
            except ObjectDoesNotExist:
                    # Do something if the doctorant does not exist
                pass
            return redirect('/radiation')
  else:
    form = RadiationForm()
  return render(request, 'webapp/radiation.html', {'form': form})


def abondant(request):
  if request.method == 'POST':
        form = AbondantForm(request.POST)
        if form.is_valid():
            fichier_nom = form.cleaned_data['fichier_nom']
            fichier = PV.objects.get(numéro=fichier_nom)
            doctorant_email = form.cleaned_data['doctorant_email']
            try:
                    doctorant = Doctorant.objects.get(email=doctorant_email)
                    doctorant.abondant = fichier
                    doctorant.statut = "Abondant"
                    doctorant.save()
            except ObjectDoesNotExist:
                    # Do something if the doctorant does not exist
                pass
            return redirect('/abondant')
  else:
    form = AbondantForm()
  return render(request, 'webapp/abondant.html', {'form': form})


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
            nouvel_Doctorant.statut='Inscrit'
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
 


