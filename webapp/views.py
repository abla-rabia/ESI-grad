from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.shortcuts import render,redirect,get_object_or_404
import os
from django.db.models import Q
from django.core.paginator import Paginator
import datetime
from django.http import  HttpResponseRedirect
import pandas as pd
from django.urls import reverse
import random
from django.core.mail import send_mail
from .decorators import allowedUsers
from django.contrib.auth.decorators import login_required


# Create your views here.













#______________les popups:___________________________#

@login_required(login_url='login')
def inscrip_pop(request):
    return render(request, 'webapp/inscrip_popup.html')



@login_required(login_url='login')
def reinscrip_pop(request):
    return render(request, 'webapp/reinscrp_popup.html')



@login_required(login_url='login')
def maj_pop(request):
    return render(request, 'webapp/maj_popup.html')


@login_required(login_url='login')
def direct_pop(request):
    return render(request, 'webapp/direct_popup.html')


@login_required(login_url='login')
def sem_pop(request):
    return render(request, 'webapp/sem_popup.html')


@login_required(login_url='login')
def  pv_pop(request):
    return render(request, 'webapp/pv_popup.html')


@login_required(login_url='login')
def  user_pop(request):
    return render(request, 'webapp/user_popup.html')



@login_required(login_url='login')
def  import_pop(request):
    return render(request, 'webapp/import_popup.html')

#_____________


@login_required(login_url='login')
def m_a_j(request):
    return render(request, 'webapp/miseajours.html')

@login_required(login_url='login')
def Aide(request):
    return render(request, 'webapp/Aide.html')


@login_required(login_url='login')
def inscrip0(request):
    return render(request, 'webapp/inscription0.html')


#______________doctorant:___________________________#


@login_required(login_url='login')
def doctorant_list(request):
    doctorants = Doctorant.objects.all()
    context = {
        'doctorants': doctorants
    }
    return render(request, 'webapp/listdoc.html', context)



@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
def doctorant_detail(request, pk):
    doctorant = get_object_or_404(Doctorant, pk=pk)
    context = {'doctorant': doctorant}
    return render(request, 'webapp/doctorant_detail.html', context)




@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
def modifier_doctorant(request, pk):
    doctorant = get_object_or_404(Doctorant, pk=pk)

    if request.method == 'POST':
        form = DoctorantForm(request.POST, instance=doctorant)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('doctorant_detail', args=(doctorant.id,)))
    else:
        form = DoctorantForm(instance=doctorant)

    return render(request, 'webapp/modifier_doctorant.html', {'form': form , 'doctorant': doctorant})






@login_required(login_url='login')
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
                search_words = nom_prénom.split()
                for word in search_words:
                 query &= Q(nom__icontains=word) | Q(prénom__icontains=word)
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
    # Tri des doctorants selon l'année d'inscription
    sort_param = request.GET.get('sort')  
    sort_reverse = request.GET.get('sort_reverse') 
    if sort_param:
        doctorants = doctorants.order_by(sort_param)  
        if sort_reverse:
            doctorants = doctorants.reverse()  
    

    paginator = Paginator(doctorants, 4) # Paginer les résultats par 10 doctorants
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'doctorants': doctorants, 'form': form,'page_obj': page_obj,'sort': sort_param}
    return render(request, 'webapp/listdoc.html', context)





#___________________________PV:___________________________#

@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
def upload_file(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid:
      file = request.FILES['file']
      ordre = request.POST['ordre']
      numéro = request.POST['numéro']
      année = request.POST['année']
      test = PV.objects.create(numéro=numéro, fichier=file, ordre_du_jour=ordre,année=année)
      test.save()
      return redirect('/fichier')
  else: 
    form = UploadFileForm()
  return render(request,'webapp/fichier.html', {'form':form})





@login_required(login_url='login')
def pv(request):
  pvs = PV.objects.all().order_by('année')
  if request.method == 'POST':
        form = RecherchePVForm(request.POST)
        if form.is_valid():
            année = form.cleaned_data['année']
            ordre = form.cleaned_data['ordre']
            query = Q()
            if année:
                query &= (Q(année=année))
            if ordre:
                query &= Q(ordre_du_jour__icontains=ordre)
            pvs = PV.objects.filter(query).order_by('année')
        else:
            pvs = PV.objects.all().order_by('année')
            form = RecherchePVForm()
  else:
        pvs = PV.objects.all().order_by('année')
        form = RecherchePVForm()


  paginator = Paginator(pvs, 7) # Paginer les résultats par 10 doctorants
  page_number = request.GET.get('page')    
  page_obj = paginator.get_page(page_number)
  context = {'pvs': pvs, 'form': form,'page_obj': page_obj}
  return render(request, 'webapp/pv.html', context) 








#_____________________Séminaire:___________________________#
@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
def add_séminaire(request):
  form = SéminaireForm()
  if request.method == 'POST':
       form = SéminaireForm(request.POST)
       if form.is_valid():
         form.save()
         return redirect('/sem_popup')

  return render(request, 'webapp/séminaire.html',  {'form':form})





@login_required(login_url='login')
def recherche_séminaire(request):
    if request.method == 'POST':
        form = RechercheSéminaireForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            type_seminaire = form.cleaned_data['type_seminaire']
            résumé=form.cleaned_data['résumé']
            query = Q()
            if titre:
                query &= (Q(titre__icontains=titre))
            if type_seminaire:
                query &= Q(type_seminaire=type_seminaire)
            if résumé:
                query &= Q(résumé__icontains=résumé)

            seminaires = Séminaire.objects.filter(query)
        else:
            seminaires = Séminaire.objects.all()
    else:
        seminaires = Séminaire.objects.all()
        form = RechercheSéminaireForm()
    paginator = Paginator(seminaires, 5) # Paginer les résultats par 10 doctorants
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'seminaires': seminaires, 'form': form,'page_obj':page_obj}
    return render(request, 'webapp/listsem.html', context)







#_____________________Encadrant:___________________________#
@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
def add_encadrant(request):
  form = EncadrantForm()
  if request.method == 'POST':
       form = EncadrantForm(request.POST)
       if form.is_valid():
         form.save()
         return redirect('/direct_popup')

  return render(request, 'webapp/encadrant.html',  {'form':form})



@login_required(login_url='login')
def recherche_encadrant(request):
    if request.method == 'POST':
        form = RechercheEncadrantForm(request.POST)
        if form.is_valid():
            nom_prénom = form.cleaned_data['nom_prénom']
            etablissement = form.cleaned_data['etablissement']
            grade = form.cleaned_data['grade']
            interets = form.cleaned_data['interets']
            query = Q()
            if nom_prénom:
                search_words = nom_prénom.split()
                for word in search_words:
                 query &= Q(nom__icontains=word) | Q(prénom__icontains=word)
            if etablissement:
                query &= Q(etablissement__icontains=etablissement)
            if grade:
                query &= Q(grade__icontains=grade)
            if interets:
                query &= Q(interets__icontains=interets)

            encadrants = Encadrant.objects.filter(query)
        else:
            encadrants = Encadrant.objects.all()
    else:
        encadrants = Encadrant.objects.all()
        form = RechercheEncadrantForm()
    paginator = Paginator(encadrants, 4) # Paginer les résultats par 10 doctorants
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'encadrants': encadrants, 'form': form,'page_obj':page_obj}
    return render(request, 'webapp/listenc.html', context)




#_____________________Acceuil:___________________________#

@login_required(login_url='login')
def Acceuil(request):
    criteres = ['option', 'type_doc','sexe'] # liste de critères possibles
    critere_choisi = random.choice(criteres) 
    tot=Doctorant.objects.all().count()
    if critere_choisi=='sexe':
        d1=Doctorant.objects.filter(sexe='Masculin').count()
        d2=Doctorant.objects.filter(sexe='Féminin').count()
        names=['Doctorants','Doctorantes']
        ma_liste=[d1,d2]
    elif critere_choisi=='option':
        d1=Doctorant.objects.filter(option='SIQ').count()
        d2=Doctorant.objects.filter(option='SI').count()
        names=['Doctorants SIQ','Doctorants SI']
        ma_liste=[d1,d2]
    elif critere_choisi=='type_doc':
        d1=Doctorant.objects.filter(type_doc='LMD').count()
        d2=Doctorant.objects.filter(type_doc='Classique').count()
        names=['Doctorants LMD','Doctorants Classiques']
        ma_liste=[d1,d2]
    
    context={
        'critere': critere_choisi,
        'ma_liste':ma_liste,
        'names':names,
        'tot':tot
    }
    return render(request,'webapp/acceuil.html',context)



#_____________________inscription:___________________________#

@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
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


@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
def inscrip2(request):
    form2 =Inscription2()
    if request.method == 'POST':
        form2 = Inscription2(request.POST)
        if form2.is_valid():
            #page2= form2.save(commit=False)
            request.session['form2_data'] = request.POST
            #form2.save()
            print("Données enregistrées avec succès !")
            return redirect('/inscription3')
        else:
            print(form2.errors)
            print("Une erreur s'est produite lors de l'enregistrement des données.")

    context = {'form2': form2}
    return render(request, 'webapp/inscrip2.html', context)



@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
def inscrip3(request):
    form3 = Inscription3()
    if request.method == 'POST':
        form3 = Inscription3(request.POST)
        if form3.is_valid():
            # Stocker les données dans la session
            request.session['form3_data'] = form3.cleaned_data
            # Créer l'objet final en combinant les données des trois pages de formulaire
            idpv = request.session['form1_data'].pop('tab_PVs', None)
            pv=PV.objects.get(id=idpv)
            email = request.session['form1_data'].get('email')
            prenom = request.session['form1_data'].get('prénom')
            

            data = {}
            data.update(request.session['form1_data'])
            data.update(request.session['form2_data'])
            data.update(request.session['form3_data'])
            
            data.pop('csrfmiddlewaretoken', None)
           

            nouvel_Doctorant = Doctorant(**data)
            nouvel_Doctorant.nbr_annees_inscription = 1
            nouvel_Doctorant.statut='Inscrit'
           
            
            nouvel_Doctorant.save()
            nouvel_Doctorant.tab_PVs.set([pv])
            email_message = f"Salem {prenom},\nNous espérons que vous allez bien! \nNous vous informons que vous êtes inscrit au Doctorat à l'ESI\nCordialement"
            send_mail(
             'Inscription Doctorat ESI', # email subject
             email_message,
             'Esigrad2023@gmail.com', # from email address
             [email], # to email addresses
             fail_silently=False, # if True, errors will be silently ignored
            )
            




            
            # Supprimer les données de session
            del request.session['form1_data']
            del request.session['form2_data']
            del request.session['form3_data']

            return redirect('/inscrip_popup')
            

    context = {'form3': form3}
    return render(request, 'webapp/inscrip3.html', context)





#____________________re_inscription:___________________________#

@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
def reinscription_normale(request) :
    form = ReinscriptionForm()
    doctorants = Doctorant.objects.filter(statut='Inscrit').order_by('nom','prénom')
    error_message = None

    if request.method == 'POST':
        form = ReinscriptionForm(request.POST)
        if form.is_valid():
            selected_pv = form.cleaned_data['pv_choice']
            selected_ids = request.POST.getlist('selections')
            if not selected_ids:
                error_message = 'Veuillez sélectionner un(des) doctorant(s) avant de valider la réinscription'
            else:
                selected_doctorants = list(Doctorant.objects.in_bulk(selected_ids).values())
                for doctorant in selected_doctorants:
                    # Update doctorant properties
                    doctorant.tab_PVs.add(selected_pv)
                    doctorant.nbr_annees_inscription += 1
                    doctorant.save()
                    #sending email
                    email=doctorant.email
                    prenom=doctorant.prénom
                    email_message = f"Salem {prenom},\nNous espérons que vous allez bien! \nNous vous informons que vous êtes re-inscrit au Doctorat à l'ESI\nCordialement"
                  
                    send_mail(
                          'RE-inscription Doctorat ESI', # email subject
                           email_message,
                          'Esigrad2023@gmail.com', # from email address
                           [email], # to email addresses
                           fail_silently=False, # if True, errors will be silently ignored
                        )
                non_selected_doctorants = list(set(doctorants) - set(selected_doctorants))
                for doctorant in non_selected_doctorants :
                    doctorant.statut = 'Différé'
                    doctorant.save()
                return redirect('/reinscription1')   
    
    # Handle GET request
    search_term = request.GET.get('search_term', '').lower().strip()
    if search_term:
        search_words = search_term.split()
        query = Q()  # Initialize an empty query object
        for word in search_words:
           query |= Q(nom__icontains=word) | Q(prénom__icontains=word)
        doctorants = doctorants.filter(query)                
    paginator = Paginator(doctorants, 5) # Paginer les résultats par 10 doctorants
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'webapp/reinscriptionnormale.html', {'form': form, 'doctorants': doctorants, 'error_message': error_message,'page_obj': page_obj})



@allowedUsers(allowedGroups=['admin'])
@login_required(login_url='login')
def reinscription_differee(request) :
    form = ReinscriptionForm()
    doctorants = Doctorant.objects.filter(statut='Différé').order_by('nom','prénom')
    error_message = None

    if request.method == 'POST':
        form = ReinscriptionForm(request.POST)
        if form.is_valid():
            selected_pv = form.cleaned_data['pv_choice']
            selected_ids = request.POST.getlist('selections')
            if not selected_ids:
                error_message = 'Veuillez sélectionner un(des) doctorant(s) avant de valider la réinscription'
            else:
                selected_doctorants = list(Doctorant.objects.in_bulk(selected_ids).values())
                for doctorant in selected_doctorants:
                    # Update doctorant properties
                    doctorant.tab_PVs.add(selected_pv)
                    doctorant.statut = 'Inscrit'
                    doctorant.nbr_annees_inscription += 1
                    doctorant.save()
                    # #sending email
                    # email=doctorant.email
                    # prenom=doctorant.prénom
                    # email_message = f"Salem {prenom},\nNous espérons que vous allez bien! \nNous vous informons que vous êtes re-inscrit au Doctorat à l'ESI\nCordialement"
# send_mail(
                    #       'RE-inscription Doctorat ESI', # email subject
                    #        email_message,
                    #       'Esigrad2023@gmail.com', # from email address
                    #        [email], # to email addresses
                    #        fail_silently=False, # if True, errors will be silently ignored
                    #     )
                non_selected_doctorants = list(set(doctorants) - set(selected_doctorants))
                for doctorant in non_selected_doctorants :
                    doctorant.radié = selected_pv
                    doctorant.statut = 'Radié'
                    doctorant.save()
                return redirect('/reinscription2') 
    
    # Handle GET request
    search_term = request.GET.get('search_term', '').lower().strip()
    if search_term:
        search_words = search_term.split()
        query = Q()  # Initialize an empty query object
        for word in search_words:
           query |= Q(nom__icontains=word) | Q(prénom__icontains=word)
        doctorants = doctorants.filter(query)  
    paginator = Paginator(doctorants, 5) # Paginer les résultats par 10 doctorants
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'webapp/reinscriptiondifferee.html', {'form': form, 'doctorants': doctorants, 'error_message': error_message,'page_obj': page_obj})


#_____________________mise à jour:___________________________#




@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
def changement_titre(request):
    form = ChangementDeTitreForm()
    doctorants = Doctorant.objects.filter(statut='Inscrit', pv_changement_titre=None).order_by('premiere_annee_inscription')
    error_message = None

    if request.method == 'POST':
        form =ChangementDeTitreForm(request.POST)
        if form.is_valid():
            selected_pv = form.cleaned_data['pv_choice']
            nv_titre = form.cleaned_data['nv_titre']
            doctorant_id = request.POST.get('selection')
            if not doctorant_id:
                error_message = 'Veuillez sélectionner un doctorant avant de valider le changement du titre'
            else:
                    doctorant = Doctorant.objects.get(id=(doctorant_id))
                    # Update doctorant properties
                    doctorant.pv_changement_titre = selected_pv
                    doctorant.nv_titre = nv_titre
                    doctorant.save() 
                    #sending email
                    email=doctorant.email
                    email_message = f"Salem {doctorant.prénom},\nNous espérons que vous allez bien!\nNous vous informons que votre demande de changement de titre de thèse est accepté.\nCordialement"
                    send_mail(
                        'Changement de titre de la thèse', # email subject
                        email_message,
                        'Esigrad2023@gmail.com', 
                        [email], 
                        fail_silently=False, 
                     )

    # Handle GET request
    search_term = request.GET.get('search_term', '').lower().strip()
    if search_term:
        search_words = search_term.split()
        queries = [Q(nom__icontains=word) | Q(prénom__icontains=word) for word in search_words]
        query = queries.pop()
        for item in queries:
            query &= item
        doctorants = doctorants.filter(query).order_by('premiere_annee_inscription')
    # Render the template with the filtered doctorants
    paginator = Paginator(doctorants, 5) # Paginer les résultats par 10 doctorants
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'webapp/changementtitre.html', {'form': form, 'doctorants': doctorants, 'error_message': error_message, 'page_obj': page_obj})





@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
def soutenance(request):
    form = SoutenanceForm()
    doctorants = Doctorant.objects.filter(statut='Inscrit').order_by('premiere_annee_inscription')
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
              doctorants = Doctorant.objects.filter(statut='Inscrit').order_by('premiere_annee_inscription')
              for doctorant_id in selected_doctorants:
                  doctorant = Doctorant.objects.get(id=int(doctorant_id))
            
                  # Update doctorant properties
                  doctorant.soutenu = selected_pv
                  doctorant.statut = "Soutenu"
                  doctorant.date_soutenance = d
                  doctorant.save() 
            
                  email = doctorant.email
                  prenom = doctorant.prénom
                  email_message = f"Salem {prenom},\nNous espérons que vous allez bien!\nNous tenons à vous féliciter pour avoir soutenu avec succès votre doctorat. Nous sommes fiers de vous et de votre réussite, et nous sommes impatients de voir ce que vous accomplirez dans votre avenir professionnel.\nCordialement"
                  send_mail(
                        'Félicitations pour votre soutenance de doctorat', # email subject
                        email_message,
                        'Esigrad2023@gmail.com', 
                        [email], 
                        fail_silently=False, 
                     )
            return redirect('/maj_popup')

    # Handle GET request
    search_term = request.GET.get('search_term', '').lower().strip()
    if search_term:
        search_words = search_term.split()
        query = Q()  # Initialize an empty query object
        for word in search_words:
           query |= Q(nom__icontains=word) | Q(prénom__icontains=word)
        doctorants = doctorants.filter(query)
    # Render the template with the filtered doctorants
    paginator = Paginator(doctorants, 5) # Paginer les résultats par 10 doctorants
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the doctorants from all pages to the template
    doctorants = Doctorant.objects.filter(statut='Inscrit').order_by('premiere_annee_inscription')
    return render(request, 'webapp/soutenance.html', {'form': form, 'doctorants': doctorants, 'error_message': error_message,'page_obj': page_obj})




@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
def radiation(request):
    form = RadiationForm()
    doctorants = Doctorant.objects.filter(Q(statut='Inscrit') | Q(statut='Différé')).order_by('premiere_annee_inscription')
    error_message = None
    if request.method == 'POST':
        form = RadiationForm(request.POST)
        if form.is_valid():
            selected_pv = form.cleaned_data['pv_choice']
            selected_doctorants = request.POST.getlist('selections')
            if not selected_doctorants:
                error_message = 'Veuillez sélectionner un(des) doctorant(s) avant de valider la radiation'
            else:
                doctorants = Doctorant.objects.filter(statut='Inscrit').order_by('premiere_annee_inscription')
                for doctorant_id in selected_doctorants:
                    doctorant = Doctorant.objects.get(id=int(doctorant_id))
                    # Update doctorant properties
                    doctorant.radié = selected_pv
                    doctorant.statut = "Radié"
                    doctorant.save()
                    email = doctorant.email
                    prenom = doctorant.prénom
                    email_message = f"Salem {prenom},\nNous espérons que vous allez bien\nNous regrettons de vous informer que, conformément à nos politiques universitaires, vous avez été radié de notre programme de doctorat.\nCordialement"
                    send_mail(
                        'Radiation..',  # email subject
                        email_message,
                        'Esigrad2023@gmail.com',
                        [email],
                        fail_silently=False,
                    )
    
    # Handle GET request
    search_term = request.GET.get('search_term', '').lower().strip()
    if search_term:
        search_words = search_term.split()
        query = Q()  # Initialize an empty query object
        for word in search_words:
            query |= Q(nom__icontains=word) | Q(prénom__icontains=word)
        doctorants = doctorants.filter(query)
    
    # Render the template with the filtered doctorants
    paginator = Paginator(doctorants, 5)  # Paginate the results by 5 doctorants
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'webapp/radiation.html',
        {'form': form, 'doctorants': doctorants, 'error_message': error_message, 'page_obj': page_obj})



    


#__________________________inscription par Excel__________________________
@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
def inscrip_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        try:
            df = pd.read_excel(excel_file)
            df['observation'] = df['observation'].fillna('')
            
            # List of mandatory columns
            mandatory_columns = ['nom', 'prénom', 'date_de_naissance', 'sexe', 'telephone', 'email', 'type_doc', 'option', 'diplome', 'etablissement_origine', 'premiere_annee_inscription', 'date_EFST', 'laboratoire', 'titre_these']
            
            # Check if all mandatory columns are not empty
            for col in mandatory_columns:
                if pd.isna(df[col]).any():
                  # Raise an error if there are null values in the mandatory columns
                  raise Exception(f"Le fichier Excel contient des valeurs manquantes pour la colonne {col} qui est une information obligatoire à remplir.")


        except Exception as e:
           message_erreur = f"Une erreur s'est produite lors de l'importation du fichier Excel : {str(e)}"
           return render(request,'webapp/inscrip_excel.html', {'message_erreur': message_erreur})
        

         # iterate over the rows of the dataframe
        for index, row in df.iterrows():
            # extract the data for the Doctorant object
            doctorant_data = {
                'nom': row['nom'],
                'prénom': row['prénom'],
                'date_de_naissance': row['date_de_naissance'],
                'sexe':row['sexe'],
                'telephone':row['telephone'],
                'email':row['email'],
                'type_doc':row['type_doc'],
                'option':row['option'],
                'diplome':row['diplome'],
                'etablissement_origine':row['etablissement_origine'],
                'premiere_annee_inscription':row['premiere_annee_inscription'],
                'date_EFST':row['date_EFST'],
                'laboratoire':row['laboratoire'],
                'titre_these':row['titre_these'],
                'observation':row['observation'],
                # add any other fields here
            }
            
            directeur_nom = row['nom_directeur']
            directeur_prénom = row['prénom_directeur']
            directeur = Encadrant.objects.get(nom=directeur_nom,prénom=directeur_prénom)

            try:
              co_directeur_nom = row['nom_co_directeur']
              co_directeur_prénom = row['prénom_co_directeur']              
              co_directeur = Encadrant.objects.get(nom=co_directeur_nom,prénom=co_directeur_prénom)
            except Encadrant.DoesNotExist:
              co_directeur = None
            

            # extract the data for the PV objects
            pvinscrip = row['PVinscrip']
            pv = PV.objects.get(numéro=pvinscrip) 

            # create the Doctorant object
            doctorant = Doctorant.objects.create(**doctorant_data)
            doctorant.nbr_annees_inscription = 1
            doctorant.statut = 'Inscrit'
            doctorant.directeur = directeur
            doctorant.co_directeur = co_directeur
            doctorant.tab_PVs.add(pv)
            doctorant.save()

        return redirect('/import_popup')
    else:
        return render(request, 'webapp/inscrip_excel.html')




#_______________________importation: initialisation de la base de donnée_______________
@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
def importation(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        df['telephone'] = df['telephone'].fillna('')
        df['email'] = df['email'].fillna('')
        df['type_doc'] = df['type_doc'].fillna('')
        df['diplome'] = df['diplome'].fillna('')  
        df['etablissement_origine'] = df['etablissement_origine'].fillna('')  
        df['nbr_annees_inscription'] = df['nbr_annees_inscription'].fillna('')
        df['email'] = df['email'].fillna('')
        df['laboratoire'] = df['laboratoire'].fillna('')
        df['nv_titre'] = df['nv_titre'].fillna('')
        df['titre_these'] = df['titre_these'].fillna('')
        df['observation'] = df['observation'].fillna('')

    


        # iterate over the rows of the dataframe
        for index, row in df.iterrows():
            # extract the data for the Doctorant object
            if pd.isna(row['date_de_naissance']):
              row['date_de_naissance'] = None
            if pd.isna(row['date_EFST']):
              row['date_EFST'] = None
            if pd.isna(row['date_soutenance']):
              row['date_soutenance'] = None 
            doctorant_data = {
                'nom': row['nom'],
                'prénom': row['prénom'],
                'date_de_naissance': row['date_de_naissance'],
                'sexe':row['sexe'],
                'telephone':row['telephone'],
                'email':row['email'],
                'type_doc':row['type_doc'],
                'option':row['option'],
                'diplome':row['diplome'],
                'etablissement_origine':row['etablissement_origine'],
                'premiere_annee_inscription':row['premiere_annee_inscription'],
                'nbr_annees_inscription':row['nbr_annees_inscription'],
                'date_EFST':row['date_EFST'],
                'laboratoire':row['laboratoire'],
                'titre_these':row['titre_these'],
                'nv_titre':row['nv_titre'],
                'date_soutenance': row['date_soutenance'],
                'statut':row['statut'],
                'observation':row['observation'],
                # add any other fields here
            }
            
            directeur_nom = row['nom_directeur']
            directeur_prénom = row['prénom_directeur']
            directeur = Encadrant.objects.get(nom=directeur_nom,prénom=directeur_prénom)

            try:
              co_directeur_nom = row['nom_co_directeur']
              co_directeur_prénom = row['prénom_co_directeur']              
              co_directeur = Encadrant.objects.get(nom=co_directeur_nom,prénom=co_directeur_prénom)
            except Encadrant.DoesNotExist:
              co_directeur = None
            
            try:
              pv_chang_num = row['pv_changement_titre']
              pv_chang = PV.objects.get(numéro=pv_chang_num)
            except PV.DoesNotExist:
              pv_chang = None
            
            try:
              pv_soute_num = row['soutenu']
              pv_soute= PV.objects.get(numéro=pv_soute_num)
            except PV.DoesNotExist:
              pv_soute = None

            try:
              pv_rad_num = row['radié']
              pv_rad  = PV.objects.get(numéro=pv_rad_num)
            except PV.DoesNotExist:
              pv_rad = None
            
            

            # extract the data for the PV objects
            pv_names = row['listePVs'].split(',')
            pv_names = [pv_name.strip() for pv_name in pv_names]
            pvs = [PV.objects.get(numéro=pv_name) for pv_name in pv_names]

            # extract the data for the Seminaire objects
           # seminaire_names = row['listeSéminaires'].split(',')
           # seminaires = [Séminaire.objects.get(titre=seminaire_name) for seminaire_name in seminaire_names]

            # create the Doctorant object
            doctorant = Doctorant.objects.create(**doctorant_data)
            doctorant.directeur = directeur
            doctorant.co_directeur = co_directeur
            doctorant.pv_changement_titre = pv_chang
            doctorant.radié = pv_rad
            doctorant.soutenu = pv_soute
            for pv in pvs:
              doctorant.tab_PVs.add(pv)
          #  for seminaire in seminaires :
          #    doctorant.tab_séminaires.add(seminaire)
            doctorant.save()

        return redirect('/import_popup')
    else:
        return render(request, 'webapp/importation.html')








