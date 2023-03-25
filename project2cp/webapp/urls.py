from django.urls import path
from . import views


urlpatterns = [
   # path('form/', views.index),
    path('fichier/', views.upload_file),
    path('séminaire/', views.add_séminaire),
]
