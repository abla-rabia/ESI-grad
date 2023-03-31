from django.urls import path
from . import views


urlpatterns = [
   # path('form/', views.index),
    path('fichier/', views.upload_file),
    path('séminaire/', views.add_séminaire),
    
    path('inscription1/', views.inscrip1, name="inscription1"),
    path('inscription2/', views.inscrip2, name="inscription2"),
    path('inscription3/', views.inscrip3, name="inscription3"),

]
