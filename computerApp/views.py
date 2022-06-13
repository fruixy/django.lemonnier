from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from computerApp.models import Machine
from computerApp.models import Personnelle
from computerApp.models import Infrastructure
from .models import Personnelle
from .forms import AddMachineForm
from .forms import AddInfrastructureForm
from .forms import AddPersonnelleForm
#from computerApp.forms import createMachineForm
# Create your views here.

def index(request) :
	context = {}
	return render(request, 'index.html', context=context)

def machine_list_view(request) :
	machines = Machine.objects.all()
	context={'machines': machines}
	return render(request, 'machine_list.html', context)

def machine_detail_view(request, pk) :
	machine = get_object_or_404(Machine, id=pk)
	context={'machine': machine}
	return render(request, 'machine_detail.html', context)


def machine_add_form(request):
	if request.method == 'POST':
		machine = AddMachineForm(request.POST or None)
		if machine.is_valid():
			machine.save()
	else:
		machine = AddMachineForm()
	context = {'machine': machine}
	return render(request, 'machine_add.html',context)

		




def personnelle_list_view(request) :
	personnelles = Personnelle.objects.all()
	context={'personnelles': personnelles}
	return render(request, 'personnelle_list.html', context)

def personnelle_detail_view(request, pk) :
	personnelle = get_object_or_404(Personnelle, id=pk)
	context={'personnelle': personnelle}
	return render(request, 'personnelle_detail.html', context)


def personnelle_add_form(request):
	if request.method == 'POST':
		personnelle = AddPersonnelleForm(request.POST or None)
		if personnelle.is_valid():
			personnelle.save()
	else:
		personnelle = AddPersonnelleForm()
	context = {'personnelle': personnelle}
	return render(request, 'personnelle_add.html',context)



def infrastructure_list_view(request):
	infrastructures = Infrastructure.objects.all()
	context={'infrastructures': infrastructures}
	return render(request, 'infrastructure_list.html', context)

def infrastructure_detail_view(request, pk) :
	infrastructure = get_object_or_404(Infrastructure, id=pk)
	context={'infrastructure': infrastructure}
	return render(request, 'infrastructure_detail.html', context)


def infrastructure_add_form(request):
	if request.method == 'POST':
		infrastructure = AddInfrastructureForm(request.POST or None)
		if infrastructure.is_valid():
			infrastructure.save()
	else:
		infrastructure = AddInfrastructureForm()
	context = {'infrastructure': infrastructure}
	return render(request, 'infrastructure_add.html',context)