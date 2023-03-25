from django.contrib import admin
from .models import *

# Register your models here.
from import_export.admin import ImportExportModelAdmin


@admin.register(Doctorant)
class userdat(ImportExportModelAdmin):
   pass

@admin.register(PV)
class userdat(ImportExportModelAdmin):
   pass

@admin.register(Séminaire)
class userdat(ImportExportModelAdmin):
   pass

@admin.register(Encadrant)
class userdat(ImportExportModelAdmin):
   pass


