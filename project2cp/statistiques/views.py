from django.shortcuts import render,redirect
from webapp.models import Doctorant
from django.http import HttpResponse
from .forms import StatistiquesForm
import datetime


def form_view(request):
    if request.method == 'GET':
        form = StatistiquesForm(request.GET)
        if form.is_valid():
            cr1 = form.cleaned_data.get('critere1')
            cr2 = form.cleaned_data.get('critere2')
            date_debut=form.cleaned_data.get('date_debut')
            if not date_debut :
                date_debut=datetime.date.min
            date_fin=form.cleaned_data.get('date_fin')
            if not date_fin :
                date_fin=datetime.date.max
            tot=Doctorant.objects.all().count()
            couleurs_fond = ['#64D1B4','#214E77', '#FEB4A9','#A77E44','#574266','#177CB0']
            if cr1 == 'sexe':
                dM=Doctorant.objects.filter(sexe='M').filter(premiere_annee_inscription__range=(date_debut, date_fin))
                dF=Doctorant.objects.filter(sexe='F').filter(premiere_annee_inscription__range=(date_debut, date_fin))
                if not cr2 : 
                    nbM=dM.count()
                    nbF=dF.count()
                    nb=2
                    names=['Doctorants','Doctorantes']
                    criteres=[cr1,cr2]
                    ma_liste = [nbM,nbF]
                elif cr2=='statut':
                    nb=6
                    nbM=dM.count()
                    nbF=dF.count()
                    #les masculins 
                    nbmins=dM.filter(statut='Inscrit').count()
                    nbmstn=dM.filter(statut='A soutenue').count()
                    nbmabd=dM.filter(statut='Abondant').count()
                    #les féminins
                    nbfins=dF.filter(statut='Inscrit').count()
                    nbfstn=dF.filter(statut='A soutenue').count()
                    nbfabd=dF.filter(statut='Abondant').count()
                    names=['Doctorants inscrits','Doctorants soutenus','Doctorants ayant abandonné','Doctorantes inscrites','Doctorantes soutenues','Doctorantes ayant abandonné']
                    criteres=[cr1,cr2]
                    ma_liste = [nbmins,nbmstn,nbmabd,nbfins,nbfstn,nbfabd]
                elif cr2=='option':
                    nb=4
                    nbM=dM.count()
                    nbF=dF.count()
                    #les masculins 
                    nbmsi=dM.filter(option='SI').count()
                    nbmsiq=dM.filter(option='SIQ').count()
                    #les féminins
                    nbfsi=dF.filter(option='SI').count()
                    nbfsiq=dF.filter(option='SIQ').count()
                    names=['Doctorants SI','Doctorants SIQ','Doctorantes SI','Doctorantes SIQ']
                    criteres=[cr1,cr2]
                    ma_liste = [nbmsi,nbmsiq,nbfsi,nbfsiq]
                elif cr2=='type_doc':
                    nb=4
                    nbM=dM.count()
                    nbF=dF.count()
                    #les masculins 
                    nbmlmd=dM.filter(type_doc='LMD').count()
                    nbmclassique=dM.filter(type_doc='Classique').count()
                    #les féminins
                    nbflmd=dF.filter(type_doc='LMD').count()
                    nbfclassique=dF.filter(type_doc='Classique').count()
                    names=['Doctorants LMD','Doctorants Classiques','Doctorantes LMD','Doctorantes Classiques']
                    criteres=[cr1,cr2]
                    ma_liste = [nbmlmd,nbmclassique,nbflmd,nbfclassique]
                
            elif cr1 == 'option':
                dSIQ=Doctorant.objects.filter(option='SIQ').filter(premiere_annee_inscription__range=(date_debut, date_fin))
                dSI=Doctorant.objects.filter(option='SI').filter(premiere_annee_inscription__range=(date_debut, date_fin))
                nbSIQ=dSIQ.count()
                nbSI=dSI.count()
                if not cr2 : 
                    nb=2
                    names=['SIQ','SI']
                    criteres=[cr1,cr2]
                    ma_liste = [nbSIQ,nbSI]
                elif cr2=='statut':
                    nb=6
                    #les siq
                    siqins=dSIQ.filter(statut='Inscrit').count()
                    siqstn=dSIQ.filter(statut='A soutenue').count()
                    siqabd=dSIQ.filter(statut='Abondant').count()
                    #les si
                    siins=dSI.filter(statut='Inscrit').count()
                    sistn=dSI.filter(statut='A soutenue').count()
                    siabd=dSI.filter(statut='Abondant').count()
                    names=['SIQ inscrits','SIQ soutenus','SIQ ayant abandonnée','SI inscrits','SI soutenus','SI ayant abandonnée']
                    criteres=[cr1,cr2]
                    ma_liste = [siqins,siqstn,siqabd,siins,sistn,siabd]
                elif cr2=='sexe':
                    nb=4
                    #les siq
                    siqm=dSIQ.filter(sexe='M').count()
                    siqf=dSIQ.filter(sexe='F').count()
                    #les si
                    sim=dSI.filter(sexe='M').count()
                    sif=dSI.filter(sexe='F').count()
                    names=['Doctorants SIQ','Doctorantes SIQ','Doctorants SI','Doctorantes SI']
                    criteres=[cr1,cr2]
                    ma_liste = [siqm,siqf,sim,sif]
                elif cr2=='type_doc':
                    nb=4
                    #les siq 
                    siqlmd=dSIQ.filter(type_doc='LMD').count()
                    siqclss=dSIQ.filter(type_doc='Classique').count()
                    #les si
                    silmd=dSI.filter(type_doc='LMD').count()
                    siclss=dSI.filter(type_doc='Classique').count()
                    names=['LMD SIQ','Classiques SIQ','LMD SI','Classiques SI']
                    criteres=[cr1,cr2]
                    ma_liste = [siqlmd,siqclss,silmd,siclss]
            elif cr1 == 'type_doc':
                dLMD=Doctorant.objects.filter(type_doc='LMD').filter(premiere_annee_inscription__range=(date_debut, date_fin))
                nbLMD=dLMD.count()
                dClss=Doctorant.objects.filter(type_doc='Classique').filter(premiere_annee_inscription__range=(date_debut, date_fin))
                nbClss=dClss.count()
                if not cr2:
                    nb=2
                    names=['LMD','Classiques']
                    criteres=[cr1,cr2]
                    ma_liste = [nbLMD,nbClss]
                elif cr2=='statut':
                    nb=6
                    #les lmd
                    lmdins=dLMD.filter(statut='Inscrit').count()
                    lmdstn=dLMD.filter(statut='A soutenue').count()
                    lmdabd=dLMD.filter(statut='Abondant').count()
                    #les classiques
                    clssins=dClss.filter(statut='Inscrit').count()
                    clssstn=dClss.filter(statut='A soutenue').count()
                    clssabd=dClss.filter(statut='Abondant').count()
                    names=['LMD inscrits','LMD soutenus','LMD ayant abandonnée','Classiques inscrits','Classiques soutenus','Classiques ayant abandonnée']
                    criteres=[cr1,cr2]
                    ma_liste = [lmdins,lmdstn,lmdabd,clssins,clssstn,clssabd]
                elif cr2=='sexe':
                    nb=4
                    #les lmd
                    lmdm=dLMD.filter(sexe='M').count()
                    lmdf=dLMD.filter(sexe='F').count()
                    #les classiques
                    clssm=dClss.filter(sexe='M').count()
                    clssf=dClss.filter(sexe='F').count()
                    names=['Doctorants LMD','Doctorantes LMD','Doctorants Classiques','Doctorantes Classiques']
                    criteres=[cr1,cr2]
                    ma_liste = [lmdm,lmdf,clssm,clssf]
                elif cr2=='option':
                    nb=4
                    #les lmd
                    lmdsi=dLMD.filter(option='SI').count()
                    lmdsiq=dLMD.filter(option='SIQ').count()
                    #les classiques
                    clsssi=dClss.filter(option='SI').count()
                    clsssiq=dClss.filter(option='SIQ').count()
                    names=['LMD SI','LMD SIQ','Classiques SI','Classiques SIQ']
                    criteres=[cr1,cr2]
                    ma_liste = [lmdsi,lmdsiq,clsssi,clsssiq]
                  
            elif cr1 == 'statut' :
                dIns=Doctorant.objects.filter(statut='Inscrit').filter(premiere_annee_inscription__range=(date_debut, date_fin))
                nbIns=dIns.count()
                dStn=Doctorant.objects.filter(statut='A soutenue').filter(premiere_annee_inscription__range=(date_debut, date_fin))
                nbStn=dStn.count()
                dAbd=Doctorant.objects.filter(statut='Abondant').filter(premiere_annee_inscription__range=(date_debut, date_fin))
                nbAbd=dAbd.count()
                if not cr2:
                    nb=3
                    names=['Inscrits','Soutenus','Ayant abandonné']
                    criteres=[cr1,cr2]
                    ma_liste = [ nbIns,nbStn,nbAbd]    
                elif cr2=='sexe':
                    nb=6
                    #les inscrits
                    insm=dIns.filter(sexe='M').count()
                    insf=dIns.filter(sexe='F').count()
                    #les abondants
                    abdm=dAbd.filter(sexe='M').count()
                    abdf=dAbd.filter(sexe='F').count()
                    #les soutenues
                    stnm=dStn.filter(sexe='M').count()
                    stnf=dStn.filter(sexe='F').count()
                    names=['Doctorants inscrits','Doctorantes inscrites','Doctorants ayant abandonné','Doctorantes ayant abandonné','Doctorants soutenus','Doctorantes soutenues']
                    criteres=[cr1,cr2]
                    ma_liste = [insm,insf,abdm,abdf,stnm,stnf]
                elif cr2=='option':
                    nb=6
                    #les inscrits
                    inssi=dIns.filter(option='SI').count()
                    inssiq=dIns.filter(option='SIQ').count()
                    #les abondants
                    abdsi=dAbd.filter(option='SI').count()
                    abdsiq=dAbd.filter(option='SIQ').count()
                    #les soutenues
                    stnsi=dStn.filter(option='SI').count()
                    stnsiq=dStn.filter(option='SIQ').count()
                    names=['SI inscrits','SIQ inscrits','SI ayant abandonnée','SIQ ayant abandonnée','SI soutenus','SIQ soutenus']
                    criteres=[cr1,cr2]
                    ma_liste = [inssi,inssiq,abdsi,abdsiq,stnsi,stnsiq]
                elif cr2=='type_doc':
                    nb=6
                    #les inscrits
                    inslmd=dIns.filter(type_doc='LMD').count()
                    insclss=dIns.filter(type_doc='Classique').count()
                    #les abondants
                    abdlmd=dIns.filter(type_doc='LMD').count()
                    abdclss=dIns.filter(type_doc='Classique').count()
                    #les soutenues
                    stnlmd=dIns.filter(type_doc='LMD').count()
                    stnclss=dIns.filter(type_doc='Classique').count()
                    names=['LMD inscrits','Classiques inscrits','LMD ayant abandonnée','Classiques ayant abandonnée','LMD soutenus','Classiques soutenus']
                    criteres=[cr1,cr2]
                    ma_liste = [inslmd,insclss,abdlmd,abdclss,stnlmd,stnclss]
            conxx={
                'ma_liste': ma_liste,
                'criteres': criteres,
                'names':names,
                'couleurs_fond':couleurs_fond
            } 
            request.session['conxx']=conxx
            return redirect('stats')

    else:
        form = StatistiquesForm()
    return render(request, 'statistiques/pages/critere.html', {'form': form})



def stats(request):
    conxx = request.session.get('conxx', {})
    ma_liste = conxx.get('ma_liste')
    criteres = conxx.get('criteres')
    names = conxx.get('names')
    couleurs_fond = conxx.get('couleurs_fond')

    return render(request, 'statistiques/pages/index.html',{'ma_liste': ma_liste,'criteres': criteres,'names':names,'couleurs_fond':couleurs_fond} ) 

def stats2(request):
    conxx = request.session.get('conxx', {})
    ma_liste = conxx.get('ma_liste')
    criteres = conxx.get('criteres')
    names = conxx.get('names')
    couleurs_fond = conxx.get('couleurs_fond')

    return render(request, 'statistiques/pages/index2.html',{'ma_liste': ma_liste,'criteres': criteres,'names':names,'couleurs_fond':couleurs_fond} ) 
