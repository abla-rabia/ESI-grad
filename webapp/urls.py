from django.urls import path
from . import views
from statistiques.views import *



urlpatterns = [
    path('Aide/', views.Aide, name="Aide"),
    path('fichier/', views.upload_file,name="fichier"),
    path('séminaire/', views.add_séminaire,name="séminaire"),
    path('encadrant/', views.add_encadrant,name="encadrant"),
    path('changementtitre/', views.changement_titre,name="changementtitre"),
    path('soutenance/', views.soutenance,name="soutnenance"),
    path('radiation/', views.radiation,name="radiation"),
    path('inscription1/', views.inscrip1, name="inscription1"),
    path('inscription2/', views.inscrip2, name="inscription2"),
    path('inscription3/', views.inscrip3, name="inscription3"),
    path('listdoc/', views.recherche_doctorant, name="listdoc"),
    path('reinscription1/', views.reinscription_normale, name="reinscriptionnormale"),
    path('reinscription2/', views.reinscription_differee, name="reinscriptiondifferee"), 
    path('inscription0/', views.inscrip0, name="inscription0"),
    path('Acceuil/', views.Acceuil, name="Acceuil"),
    path('miseajour/', views.m_a_j, name="miseajour"),
    path('pv/',views.pv,name="pv"),
    path('inscrip_popup/',views.inscrip_pop,name="inscrip_popup"),
    path('reinscrip_popup/',views.reinscrip_pop,name="reinscrip_popup"),
    path('maj_popup/',views.maj_pop,name="maj_popup"),
    path('direct_popup/',views.direct_pop,name="direct_popup"),
    path('sem_popup/',views.sem_pop,name="sem_popup"),
    path('pv_popup/',views.pv_pop,name="pv_popup"),
    path('user_popup/',views.user_pop,name="user_popup"),
    path('import_popup/',views.import_pop,name="import_popup"),
    path('doctorant/<int:pk>/', views.doctorant_detail, name='doctorant_detail'),
    path('doctorant/<int:pk>/modifier/', views.modifier_doctorant, name='modifier_doctorant'),
    path('listsem/', views.recherche_séminaire, name="listsem"),
    path('listenc/', views.recherche_encadrant, name="listenc"),
    path('inscriptionexcel/',views.inscrip_excel,name="inscriptionexcel"),
    path('importation/',views.importation,name="importation"),
]
