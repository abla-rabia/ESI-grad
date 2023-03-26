from django.shortcuts import render
from webapp.models import Doctorant

# Create your views here.
def index(request):
    return render(request,'statistiques/index.html')
