from django.urls import path
from . import views
from webapp.views import *
urlpatterns = [
    path('', views.form_view, name='form_view'),
    path('01/',views.stats,name='stats'),
    path('02/',views.stats2,name='stats2'),
]
