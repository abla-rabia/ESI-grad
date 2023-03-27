from django.urls import path
from . import views


urlpatterns = [
    path('fichier/', views.upload_file),
    path('séminaire/', views.add_séminaire),
    path('encadrant/',views.add_encadrant),
]
