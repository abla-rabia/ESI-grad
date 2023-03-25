from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render,redirect
import os

# Create your views here.

""""
def index(request):
    form = DoctorantForm()

    if request.method == 'POST':
       form = DoctorantForm(request.POST)
       if form.is_valid():
         form.save()
         return redirect('/form')
        
    context = {'form':form}
    return render(request, 'webapp/index.html', context)

"""

def upload_file(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid:
      file = request.FILES['file']
      file_name, file_ext = os.path.splitext(file.name)  # get the filename and extension of the uploaded file
      test = PV.objects.create(numéro=file_name, fichier=file)
      test.save()
      return HttpResponse("The name of uploaded file is " + str(file) + "in PV" + str(test.pk))
  else: 
    form = UploadFileForm()
  return render(request,'webapp/fichier.html', {'form':form})


def add_séminaire(request):
  form = SéminaireForm()
  if request.method == 'POST':
       form = SéminaireForm(request.POST)
       if form.is_valid():
         form.save()
         return redirect('/séminaire')

  return render(request, 'webapp/séminaire.html',  {'form':form})