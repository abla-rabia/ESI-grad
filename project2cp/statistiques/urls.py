from django.urls import path
from . import views
urlpatterns = [
    path('', views.form_view, name='form_view'),
    path('01/',views.stats,name='stats'),
    path('02/',views.stats2,name='stats2'),
]
