from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cours, Professeur, Classe

class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'specialite', 'email')
    search_fields = ('nom', 'prenom')

class ClasseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_classe', 'niveau', 'effectif')
    search_fields = ('nom_classe', 'niveau')

class CoursAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'professeur', 'classe', 'date_debut')
    search_fields = ('titre',)

admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Cours, CoursAdmin)