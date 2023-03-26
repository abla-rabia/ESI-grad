from django.shortcuts import render
from webapp.models import Doctorant

# Create your views here.
def index(request):
    doc=Doctorant.objects.filter(type_doc='LMD')
    doc2=Doctorant.objects.filter(type_doc='Classique')
    count={'doc' : doc.count(),'doc2' : doc2.count()}
    return render(request,'statistiques/index.html',count)
