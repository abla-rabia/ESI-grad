from django.db import models

# Create your models here.
class PV(models.Model):
    numéro = models.CharField(max_length=100, null=True)
    fichier = models.FileField(null=True)
    ordre_du_jour = models.CharField(max_length=1000, null=True)
    année = models.CharField(max_length=10, null=True)

    def __str__(self):
       return self.numéro

class Séminaire(models.Model):
    TYPE_SEMINAIRE = (
        ('Interne', 'Interne'),
        ('Externe', 'Externe'),
    )
    titre = models.CharField(max_length=100, null=True)
    type_seminaire = models.CharField(max_length=100, null=True, choices=TYPE_SEMINAIRE)
    résumé=models.CharField(max_length=1000, null=True)

    def __str__(self):
       return self.titre

class Encadrant(models.Model):
    nom = models.CharField(max_length=100, null=True)
    prénom = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    etablissement = models.CharField(max_length=100, null=True)
    laboratoire = models.CharField(max_length=100, null=True)
    grade = models.CharField(max_length=100, null=True)
    interets =  models.CharField(max_length=1000, null=True)

    def __str__(self):
       return f"{self.nom} {self.prénom}"

class Doctorant(models.Model): 
    SEXE = (
       ('Masculin', 'Masculin'),
       ('Féminin', 'Féminin'),
    )

    TYPE_DOC = (
        ('LMD', 'LMD'),
        ('Classique', 'Classique'),
    )
    
    DIPLOME = (
        ('Master', 'Master'),
        ('Magister', 'Magister'),
        ('Ingéniorat', 'Ingéniorat'),
    )

    STATUT =(
        ('Inscrit', 'Inscrit'),
        ('Soutenu', 'Soutenu'),
        ('Différé', 'Différé'),
        ('Radié', 'Radié'),
    )

    OPTION = {
        ('SI','SI'),
        ('SIQ','SIQ'),
    }

    nom = models.CharField(max_length=100, null=True)
    prénom = models.CharField(max_length=100, null=True)
    date_de_naissance = models.DateField(null=True)
    sexe = models.CharField(max_length=10, null=True, choices=SEXE)
    telephone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    type_doc =  models.CharField(max_length=50, null=True, choices=TYPE_DOC)
    option = models.CharField(max_length=100, null=True,choices=OPTION)
    diplome = models.CharField(max_length=100, null=True, choices=DIPLOME)
    etablissement_origine = models.CharField(max_length=100, null=True)
    premiere_annee_inscription = models.CharField(max_length=100, null=True)
    nbr_annees_inscription = models.IntegerField(null=True)
    date_EFST = models.DateField(null=True)
    laboratoire = models.CharField(max_length=100, null=True)
    directeur = models.ForeignKey(Encadrant, null=True, on_delete=models.SET_NULL)
    co_directeur = models.ForeignKey(Encadrant, on_delete=models.SET_NULL, related_name="co_dir",blank=True,null=True)
    titre_these = models.CharField(max_length=300, null=True)
    nv_titre = models.CharField(max_length=300, null=True)
    pv_changement_titre = models.ForeignKey(PV, null=True, on_delete=models.SET_NULL, related_name="changement")
    radié = models.ForeignKey(PV, null=True,on_delete=models.SET_NULL, related_name="radié")
    soutenu = models.ForeignKey(PV, null=True, on_delete=models.SET_NULL, related_name="soutenu")
    date_soutenance = models.DateField(null=True)
    tab_PVs = models.ManyToManyField(PV)
    tab_séminaires = models.ManyToManyField(Séminaire,blank=True)
    statut = models.CharField(max_length=50, null=True, choices=STATUT)
    observation = models.CharField(max_length=300, null=True,blank=True)

    def __str__(self):
        return f"{self.nom} {self.prénom}"