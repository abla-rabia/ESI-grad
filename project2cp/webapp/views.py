from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.shortcuts import render,redirect
import os
from django.db.models import Q
import datetime


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
    form = ReinscriptionForm()
    doctorants = Doctorant.objects.all().order_by('nom','prénom')
    error_message = None

    if request.method == 'POST':
        form = ReinscriptionForm(request.POST)
        if form.is_valid():
            print('hello2')
            selected_pv = form.cleaned_data['pv_choice']
            print(selected_pv)
            selected_doctorants = request.POST.getlist('selections')
            print(selected_doctorants)
            if not selected_doctorants:
                error_message = 'Veuillez sélectionner un(des) doctorant(s) avant de valider la réinscription'
            else:
                for doctorant_id in selected_doctorants:
                    doctorant = Doctorant.objects.get(pk=int(doctorant_id))
                    # Update doctorant properties
                    doctorant.tab_PVs.add(selected_pv)
                    doctorant.nbr_annees_inscription += 1
                    doctorant.save()
            return redirect('/reinscription')   
    return render(request, 'webapp/reinscription.html', {'form': form, 'doctorants': doctorants, 'error_message': error_message})
 
             
    # Handle GET request
    search_term = request.GET.get('search_term', '').lower().strip()
    if search_term:
        search_words = search_term.split()
        queries = [Q(nom__icontains=word) | Q(prénom__icontains=word) for word in search_words]
        query = queries.pop()
        for item in queries:
            query &= item
        doctorants = doctorants.filter(query)
    # Render the template with the filtered doctorants 



def changement_titre(request):
    form = ChangementDeTitreForm()
    doctorants = Doctorant.objects.all().order_by('nom','prénom')
    error_message = None

    if request.method == 'POST':
        form =ChangementDeTitreForm(request.POST)
        if form.is_valid():
            selected_pv = form.cleaned_data['pv_choice']
            nv_titre = form.cleaned_data['nv_titre']
            selected_doctorants = request.POST.getlist('selections')
            if not selected_doctorants:
                error_message = 'Veuillez sélectionner un(des) doctorant(s) avant de valider le changement du titre'
            else:
              for doctorant_id in selected_doctorants:
                    doctorant = Doctorant.objects.get(id=int(doctorant_id))
                    # Update doctorant properties
                    doctorant.pv_changement_titre = selected_pv
                    doctorant.nv_titre = nv_titre
                    doctorant.save() 

    # Handle GET request
    search_term = request.GET.get('search_term', '').lower().strip()
    if search_term:
        search_words = search_term.split()
        queries = [Q(nom__icontains=word) | Q(prénom__icontains=word) for word in search_words]
        query = queries.pop()
        for item in queries:
            query &= item
        doctorants = doctorants.filter(query)
    # Render the template with the filtered doctorants
    
    return render(request, 'webapp/changementtitre.html', {'form': form, 'doctorants': doctorants, 'error_message': error_message})



def soutenance(request):
    form = SoutenanceForm()
    doctorants = Doctorant.objects.all().order_by('nom','prénom')
    error_message = None

    if request.method == 'POST':
        form = SoutenanceForm(request.POST)
        if form.is_valid():
            selected_pv = form.cleaned_data['pv_choice']
            d = form.cleaned_data['date']
            selected_doctorants = request.POST.getlist('selections')
            if not selected_doctorants:
                error_message = 'Veuillez sélectionner un(des) doctorant(s) avant de valider la soutenance'
            else:
              for doctorant_id in selected_doctorants:
                    doctorant = Doctorant.objects.get(id=int(doctorant_id))
                    # Update doctorant properties
                    doctorant.a_soutenue = selected_pv
                    doctorant.status = "A soutenue"
                    doctorant.date_soutenance = d
                    doctorant.save() 

    # Handle GET request
    search_term = request.GET.get('search_term', '').lower().strip()
    if search_term:
        search_words = search_term.split()
        queries = [Q(nom__icontains=word) | Q(prénom__icontains=word) for word in search_words]
        query = queries.pop()
        for item in queries:
            query &= item
        doctorants = doctorants.filter(query)
    # Render the template with the filtered doctorants
    
    return render(request, 'webapp/soutenance.html', {'form': form, 'doctorants': doctorants, 'error_message': error_message})


def radiation(request):
    form = RadiationForm()
    doctorants = Doctorant.objects.all().order_by('nom','prénom')
    error_message = None

    if request.method == 'POST':
        form = RadiationForm(request.POST)
        if form.is_valid():
            selected_pv = form.cleaned_data['pv_choice']
            selected_doctorants = request.POST.getlist('selections')
            if not selected_doctorants:
                error_message = 'Veuillez sélectionner un(des) doctorant(s) avant de valider la radiation'
            else:
              for doctorant_id in selected_doctorants:
                    doctorant = Doctorant.objects.get(id=int(doctorant_id))
                    # Update doctorant properties
                    doctorant.radié = selected_pv
                    doctorant.status = "Radié"
                    doctorant.save() 

    # Handle GET request
    search_term = request.GET.get('search_term', '').lower().strip()
    if search_term:
        search_words = search_term.split()
        queries = [Q(nom__icontains=word) | Q(prénom__icontains=word) for word in search_words]
        query = queries.pop()
        for item in queries:
            query &= item
        doctorants = doctorants.filter(query)
    # Render the template with the filtered doctorants
    
    return render(request, 'webapp/radiation.html', {'form': form, 'doctorants': doctorants, 'error_message': error_message})



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
 


def recherche_doctorant(request):
    if request.method == 'POST':
        form = RechercheDoctorantForm(request.POST)
        if form.is_valid():
            nom_prénom = form.cleaned_data['nom_prénom']
            date_debut = form.cleaned_data['date_debut']
            date_fin = form.cleaned_data['date_fin']
            if not date_debut :
                date_debut=datetime.date.min
            date_fin=form.cleaned_data.get('date_fin')
            if not date_fin :
                date_fin=datetime.date.max
            sexe=form.cleaned_data['sexe']
            option=form.cleaned_data['option']
            statut=form.cleaned_data['statut']
            type_doc=form.cleaned_data['type_doc']
            query = Q()
            if nom_prénom:
                query &= (Q(nom__icontains=nom_prénom) | Q(prénom__icontains=nom_prénom))
            if date_debut:
                query &= Q(premiere_annee_inscription__range=(date_debut, date_fin))
            if date_fin:
                query &= Q(premiere_annee_inscription__range=(date_debut, date_fin))
            if sexe:
                query &= Q(sexe=sexe)
            if option:
                query &= Q(option=option)
            if statut:
                query &= Q(statut=statut)
            if type_doc:
                query &= Q(type_doc=type_doc)

            doctorants = Doctorant.objects.filter(query)
        else:
            doctorants = Doctorant.objects.all()
    else:
        doctorants = Doctorant.objects.all()
        form = RechercheDoctorantForm()

    context = {'doctorants': doctorants, 'form': form}
    return render(request, 'webapp/listdoc.html', context)


def pv(request):
  pvs = PV.objects.all().order_by('numéro')
  return render(request, 'webapp/pv.html', {'pvs': pvs})