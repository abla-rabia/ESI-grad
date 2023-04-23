from django.urls import path
from . import views



urlpatterns = [
    path('fichier/', views.upload_file,name="fichier"),
    path('séminaire/', views.add_séminaire),
    path('encadrant/', views.add_encadrant),
    path('reinscription/', views.reinscription, name="reinscription"),
    path('changementtitre/', views.changement_titre,name="changementtitre"),
    path('soutenance/', views.soutenance,name="soutnenance"),
    path('radiation/', views.radiation,name="radiation"),
    path('abondant/', views.abondant,name="abondant"),
    path('inscription1/', views.inscrip1, name="inscription1"),
    path('inscription2/', views.inscrip2, name="inscription2"),
    path('inscription3/', views.inscrip3, name="inscription3"),
    path('listusers/', views.user_list, name="listusers"),
    path('listdoc/', views.doctorant_list, name="listdoc"),

    
    path('inscription0/', views.inscrip0, name="inscription0"),
    path('Acceuil/', views.Acceuil, name="Acceuil"),
    path('miseajour/', views.m_a_j, name="miseajour"),

]
