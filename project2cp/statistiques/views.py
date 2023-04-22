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
            date_debut=form.cleaned_data('date_debut')
            if not date_debut :
                date_debut=datetime.date.min
            date_fin=form.cleaned_data('date_fin')
            if not date_fin :
                date_fin=datetime.date.max
            tot=Doctorant.objects.all().count()
            if cr1 == 'sexe':
                dM=Doctorant.objects.filter(sexe='M').filter(date__range=(date_debut, date_fin))
                dF=Doctorant.objects.filter(sexe='F').filter(date__range=(date_debut, date_fin))
                if not cr2 : 
                    nbM=dM.count()
                    nbF=dF.count()
                    ma_liste = [cr1, cr2, nbM,nbF,int(tot)]
                elif cr2=='statut':
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
                    ma_liste = [cr1, cr2, nbM,nbF,nbmins,nbmstn,nbmabd,nbfins,nbfstn,nbfabd,int(tot)]
                elif cr2=='option':
                    nbM=dM.count()
                    nbF=dF.count()
                    #les masculins 
                    nbmsi=dM.filter(option='SI').count()
                    nbmsiq=dM.filter(option='SIQ').count()
                    #les féminins
                    nbfsi=dF.filter(option='SI').count()
                    nbfsiq=dF.filter(option='SIQ').count()
                    ma_liste = [cr1, cr2, nbM,nbF,nbmsi,nbmsiq,nbfsi,nbfsiq,int(tot)]
                elif cr2=='type_doc':
                    nbM=dM.count()
                    nbF=dF.count()
                    #les masculins 
                    nbmlmd=dM.filter(type_doc='LMD').count()
                    nbmclassique=dM.filter(type_doc='Classique').count()
                    #les féminins
                    nbflmd=dF.filter(type_doc='LMD').count()
                    nbfclassique=dF.filter(type_doc='Classique').count()
                    ma_liste = [cr1, cr2, nbM,nbF,nbmlmd,nbmclassique,nbflmd,nbfclassique,int(tot)]
                
            elif cr1 == 'option':
                dSIQ=Doctorant.objects.filter(option='SIQ').filter(date__range=(date_debut, date_fin))
                dSI=Doctorant.objects.filter(option='SI').filter(date__range=(date_debut, date_fin))
                nbSIQ=dSIQ.count()
                nbSI=dSI.count()
                if not cr2 : 
                    ma_liste = [cr1, cr2, nbSIQ,nbSI,int(tot)]
                elif cr2=='statut':
                    #les siq
                    siqins=dSIQ.filter(statut='Inscrit').count()
                    siqstn=dSIQ.filter(statut='A soutenue').count()
                    siqabd=dSIQ.filter(statut='Abondant').count()
                    #les si
                    siins=dSI.filter(statut='Inscrit').count()
                    sistn=dSI.filter(statut='A soutenue').count()
                    siabd=dSI.filter(statut='Abondant').count()
                    ma_liste = [cr1, cr2, nbSI,nbSIQ,siqins,siqstn,siqabd,siins,sistn,siabd,int(tot)]
                elif cr2=='sexe':
                    #les siq
                    siqm=dSIQ.filter(sexe='M').count()
                    siqf=dSIQ.filter(sexe='F').count()
                    #les si
                    sim=dSI.filter(sexe='M').count()
                    sif=dSI.filter(sexe='F').count()
                    ma_liste = [cr1, cr2, nbSI,nbSIQ,siqm,siqf,sim,sif,int(tot)]
                elif cr2=='type_doc':
                    #les siq 
                    siqlmd=dSIQ.filter(type_doc='LMD').count()
                    siqclss=dSIQ.filter(type_doc='Classique').count()
                    #les si
                    silmd=dSI.filter(type_doc='LMD').count()
                    siclss=dSI.filter(type_doc='Classique').count()
                    ma_liste = [cr1, cr2, nbSIQ,nbSI,siqlmd,siqclss,silmd,siclss,int(tot)]
            elif cr1 == 'type_doc':
                dLMD=Doctorant.objects.filter(type_doc='LMD').filter(date__range=(date_debut, date_fin))
                nbLMD=dLMD.count()
                dClss=Doctorant.objects.filter(type_doc='Classique').filter(date__range=(date_debut, date_fin))
                nbClss=dClss.count()
                if not cr2:
                    ma_liste = [cr1, cr2, nbLMD,nbClss,int(tot)]
                elif cr2=='statut':
                    #les lmd
                    lmdins=dLMD.filter(statut='Inscrit').count()
                    lmdstn=dLMD.filter(statut='A soutenue').count()
                    lmdabd=dLMD.filter(statut='Abondant').count()
                    #les classiques
                    clssins=dClss.filter(statut='Inscrit').count()
                    clssstn=dClss.filter(statut='A soutenue').count()
                    clssabd=dClss.filter(statut='Abondant').count()
                    ma_liste = [cr1, cr2, nbLMD,nbClss,lmdins,lmdstn,lmdabd,clssins,clssstn,clssabd,int(tot)]
                elif cr2=='sexe':
                    #les lmd
                    lmdm=dLMD.filter(sexe='M').count()
                    lmdf=dLMD.filter(sexe='F').count()
                    #les classiques
                    clssm=dClss.filter(sexe='M').count()
                    clssf=dClss.filter(sexe='F').count()
                    ma_liste = [cr1, cr2, nbLMD,nbClss,lmdm,lmdf,clssm,clssf,int(tot)]
                elif cr2=='option':
                    #les lmd
                    lmdsi=dLMD.filter(option='SI').count()
                    lmdsiq=dLMD.filter(option='SIQ').count()
                    #les classiques
                    clsssi=dClss.filter(option='SI').count()
                    clsssiq=dClss.filter(option='SIQ').count()
                    ma_liste = [cr1, cr2, nbLMD,nbClss,lmdsi,lmdsiq,clsssi,clsssiq,int(tot)]
                  
            elif cr1 == 'statut' :
                dIns=Doctorant.objects.filter(statut='Inscrit').filter(date__range=(date_debut, date_fin))
                nbIns=dIns.count()
                dStn=Doctorant.objects.filter(statut='A soutenue').filter(date__range=(date_debut, date_fin))
                nbStn=dStn.count()
                dAbd=Doctorant.objects.filter(statut='Abondant').filter(date__range=(date_debut, date_fin))
                nbAbd=dAbd.count()
                if not cr2:
                    ma_liste = [cr1, cr2, nbIns,nbStn,nbAbd,int(tot)]    
                elif cr2=='sexe':
                    #les inscrits
                    insm=dIns.filter(sexe='M').count()
                    insf=dIns.filter(sexe='F').count()
                    #les abondants
                    abdm=dAbd.filter(sexe='M').count()
                    abdf=dAbd.filter(sexe='F').count()
                    #les soutenues
                    stnm=dStn.filter(sexe='M').count()
                    stnf=dStn.filter(sexe='F').count()
                    ma_liste = [cr1, cr2, nbIns,nbStn,nbAbd,insm,insf,abdm,abdf,stnm,stnf,int(tot)]
                elif cr2=='option':
                    #les inscrits
                    inssi=dIns.filter(option='SI').count()
                    inssiq=dIns.filter(option='SIQ').count()
                    #les abondants
                    abdsi=dAbd.filter(option='SI').count()
                    abdsiq=dAbd.filter(option='SIQ').count()
                    #les soutenues
                    stnsi=dStn.filter(option='SI').count()
                    stnsiq=dStn.filter(option='SIQ').count()
                    ma_liste = [cr1, cr2, nbIns,nbStn,nbAbd,inssi,inssiq,abdsi,abdsiq,stnsi,stnsiq,int(tot)]
                elif cr2=='type_doc':
                    #les inscrits
                    inslmd=dIns.filter(type_doc='LMD').count()
                    insclss=dIns.filter(type_doc='Classique').count()
                    #les abondants
                    abdlmd=dIns.filter(type_doc='LMD').count()
                    abdclss=dIns.filter(type_doc='Classique').count()
                    #les soutenues
                    stnlmd=dIns.filter(type_doc='LMD').count()
                    stnclss=dIns.filter(type_doc='Classique').count()
                    ma_liste = [cr1, cr2, nbIns,nbStn,nbAbd,inslmd,insclss,abdlmd,abdclss,stnlmd,stnclss,int(tot)]
                
            stats={
                    'ma_liste': ma_liste
            } 
            return render(request, 'statistiques/pages/index.html', stats)
    else:
        form = StatistiquesForm()
    return render(request, 'statistiques/pages/critere.html', {'form': form})
