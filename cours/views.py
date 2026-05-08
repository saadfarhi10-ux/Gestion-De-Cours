from django.shortcuts import render, redirect
from .models import Cours, Professeur, Classe
from .forms import GestionCours, GestionProfesseur, GestionClasse


def index(request):
    cours = Cours.objects.all()
    return render(request, 'cours/index.html', {'cours': cours})


def ajoutCours(request):
    form = GestionCours(request.POST or None)

    if form.is_valid():
        titre = form.cleaned_data['titre']
        description = form.cleaned_data['description']
        professeur = form.cleaned_data['professeur']
        classe = form.cleaned_data['classe']
        date_debut = form.cleaned_data['date_debut']

        nouveau_cours = Cours(
            titre=titre,
            description=description,
            professeur=professeur,
            classe=classe,
            date_debut=date_debut
        )
        nouveau_cours.save()
        form = GestionCours()

    return render(request, 'cours/ajoutCours.html', {'form': form})

def editCours(request, cours_id):
    cours = Cours.objects.get(id=cours_id)

    form = GestionCours(request.POST or None, initial={
        'titre': cours.titre,
        'description': cours.description,
        'professeur': cours.professeur,
        'classe': cours.classe,
        'date_debut': cours.date_debut,
    })

    if form.is_valid():
        cours.titre = form.cleaned_data['titre']
        cours.description = form.cleaned_data['description']
        cours.professeur = form.cleaned_data['professeur']
        cours.classe = form.cleaned_data['classe']
        cours.date_debut = form.cleaned_data['date_debut']
        cours.save()
        return redirect('cours_index')

    return render(request, 'cours/editCours.html', {'form': form, 'cours': cours})

def deleteCours(request, cours_id):
    cours = Cours.objects.get(id=cours_id)
    cours.delete()
    return redirect('cours_index')

def listeProfesseurs(request):
    professeurs = Professeur.objects.all()
    return render(request, 'cours/listeProfesseurs.html', {'professeurs': professeurs})


def listeClasses(request):
    classes = Classe.objects.all()
    return render(request, 'cours/listeClasses.html', {'classes': classes})

def ajoutClasse(request):
    form = GestionClasse(request.POST or None)
    if form.is_valid():
        classe = Classe(
            nom_classe=form.cleaned_data['nom_classe'],
            niveau=form.cleaned_data['niveau'],
            effectif=form.cleaned_data['effectif']
        )
        classe.save()
        form = GestionClasse()
    return render(request, 'cours/ajoutClasse.html', {'form': form})

def deleteClasse(request, classe_id):
    classe = Classe.objects.get(id=classe_id)
    classe.delete()
    return redirect('liste_classes')