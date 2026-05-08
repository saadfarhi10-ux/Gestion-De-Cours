from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Professeur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    specialite = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Classe(models.Model):
    nom_classe = models.CharField(max_length=200)
    niveau = models.CharField(max_length=200)
    effectif = models.IntegerField()

    def __str__(self):
        return f"{self.nom_classe} ({self.niveau})"


class Cours(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titre