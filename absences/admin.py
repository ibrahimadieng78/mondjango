from django.contrib import admin

from GestionAbsences.absences.models import Absence, Cours, Etudiant
admin.site.register(Etudiant)
admin.site.register(Cours)
admin.site.register(Absence)


# Register your models here.
