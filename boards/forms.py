  
from django import forms
from .models import Annonce




class AnnonceForm(forms.ModelForm):

    class Meta:
        model = Annonce
        fields = ('TypeLogement','NombreChambre','Surface','Emplacement','description','photo',)




