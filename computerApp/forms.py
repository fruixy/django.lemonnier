from django import forms
from django.core.exceptions import ValidationError
from computerApp.models import Machine
from computerApp.models import Personnelle
from computerApp.models import Infrastructure


class AddMachineForm(forms.Form) :

    nom_machine = forms.CharField(required=True, label="Nom de la machine")

    def clean_nom(self):
        data = self.cleaned_data['nom']
        if len(data) != 6:
            raise ValidationError(("Erreur de format pour le champs 'nom'"))
        
        return data


class AddInfrastructureForm(forms.Form):
    
    nom_infra=forms.CharField(label="nom infrastructure")
    
    def clean_infra(self):
        data=self.cleaned_data["nom"]
        if len(data) != 1:
            raise ValidationError(("erreur de format pour le champs 'nom'"))
        
        return data
        

class AddPersonnelleForm(forms.Form):
    
    nom_perso=forms.CharField(label="personnelle")
    
    def clean_personnelle(self):
        data=self.cleaned_data["nom"]
        if len(data) != 1:
            raise ValidationError(("erreur de format pour le champs 'nom'"))
        
        return data