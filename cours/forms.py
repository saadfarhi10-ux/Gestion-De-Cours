from django import forms
from .models import Cours, Professeur, Classe

class GestionCours(forms.Form):
    titre = forms.CharField(
        label="Titre :",
        max_length=255,
        required=True
    )
    description = forms.CharField(
        label="Description :",
        required=False,
        widget=forms.Textarea
    )
    professeur = forms.ModelChoiceField(
        label="Professeur :",
        queryset=Professeur.objects.all(),
        required=True
    )
    classe = forms.ModelChoiceField(
        label="Classe :",
        queryset=Classe.objects.all(),
        required=True
    )
    date_debut = forms.DateField(
        label="Date de début :",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )


class GestionProfesseur(forms.Form):
    nom = forms.CharField(
        label="Nom :",
        max_length=200,
        required=True
    )
    prenom = forms.CharField(
        label="Prénom :",
        max_length=200,
        required=True
    )
    specialite = forms.CharField(
        label="Spécialité :",
        max_length=200,
        required=True
    )
    email = forms.EmailField(
        label="Email :",
        required=True
    )


class GestionClasse(forms.Form):
    nom_classe = forms.CharField(
        label="Nom de la classe :",
        max_length=200,
        required=True
    )
    niveau = forms.CharField(
        label="Niveau :",
        max_length=200,
        required=True
    )
    effectif = forms.IntegerField(
        label="Effectif :",
        required=True
    )