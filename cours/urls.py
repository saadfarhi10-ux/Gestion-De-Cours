from django.urls import path
from . import views

urlpatterns = [
    # Cours
    path('', views.index, name='cours_index'),
    path('ajoutCours/', views.ajoutCours, name='ajout_cours'),
    path('editCours/<int:cours_id>/', views.editCours, name='edit_cours'),
    path('deleteCours/<int:cours_id>/', views.deleteCours, name='delete_cours'),

    # Professeurs
    path('professeurs/', views.listeProfesseurs, name='liste_professeurs'),

    # Classes
    path('classes/', views.listeClasses, name='liste_classes'),
    path('ajoutClasse/', views.ajoutClasse, name='ajout_classe'),
    path('deleteClasse/<int:classe_id>/', views.deleteClasse, name='delete_classe'),
]