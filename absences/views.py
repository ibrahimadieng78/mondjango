from django.shortcuts import get_object_or_404, render
from .models import Etudiant
from .models import Cours
from .models import Absence

def liste_etudiants(request):
     etudiant = Etudiant.objects.all()
     return render(request, 'Absences/liste_etudiants.html', {'etudiant': etudiant})
def liste_cours(request):
     cours=Cours.objects.all()
     return render(request, 'Absences/liste_cours.html',{'cours': cours})
def enregistrer_Absences(request,etudiant_id,cours_id):
     etudiant=get_object_or_404(Etudiant,pk=etudiant_id)
     cours=get_object_or_404(Cours,pk=cours)

     if request.method =='POST':
          justifiee=request.POST.get('justifiée',False)
          absence=Absence(etudiant=etudiant,cours=cours,justifiee=justifiee)
          absence.save()
     return render(request,'Absences/liste_Absences.html', {'etudiant': etudiant,'cours':cours})