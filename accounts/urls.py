from django.urls import path
from . import views
from statistiques.views import *



urlpatterns = [

path('login/', views.My_login, name='login'),
path('', views.welcome ,name='welcome'),
path('apropos', views.a_propos ,name='apropos'),
path('contact', views.contact ,name='contact'),
path('logout/', views.userlogout , name="logout"),
path('register/', views.register , name="register"),
path('add_user/', views.add_user , name="add_user"),
path('list_user/', views.user_list , name="list_user"),
]
