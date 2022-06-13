from django import forms
from django.core.exceptions import ValidationError
from computerApp.models import Machine
from computerApp.models import Personnelle
from computerApp.models import Infrastructure

#on reprends les models pour faire des formulaires

#formulaire pour créer des machines
class AddMachineForm(forms.ModelForm) :
    class Meta:
        model = Machine
        fields = ('nom', 'utilisateur', 'responsable', 'infrastructure', 'maintenanceDate', 'mach')

#formulaire pour créer des personnelles
class AddPersonnelleForm(forms.ModelForm):
    class Meta:
        model = Personnelle
        fields = ('nom', 'prenom', 'infrastructure', 'email', 'num', 'date_entree')
        

#formulaire pour créer des infrastructures
class AddInfrastructureForm(forms.ModelForm):
    class Meta:
        model = Infrastructure
        fields = ('infrastructure','responsable', 'maintenanceDate', 'date_creation')