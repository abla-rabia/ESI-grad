from django.shortcuts import render
from webapp.models import Doctorant

# Create your views here.
def index(request):
    context = {
        'allDoct' : Doctorant.objects.all().count(),
        'fDoct' : Doctorant.objects.filter(sexe='F').count(),
        'mDoct' : Doctorant.objects.filter(sexe='M').count(),
    }
    return render(request,'statistiques/pages/index.html',context)
