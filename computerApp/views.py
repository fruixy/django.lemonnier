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
	nb_machines = Machine.objects.count()
	nb_infrastrutures = Infrastructure.objects.count()
	machines = Machine.objects.order_by('maintenanceDate')
	infrastructures = Infrastructure.objects.order_by('maintenanceDate')
	context = {
		'nb_infrastructures' : nb_infrastrutures,
		'nb_machines' : nb_machines,
		'machines': machines,
		'infrastructures': infrastructures
	}
	return render(request, 'index.html', context)

	



def machine_list_view(request) :
	nb_machines = Machine.objects.count()
	machines = Machine.objects.all()
	context={
		'nb_machines' : nb_machines,
		'machines': machines
		}
	return render(request, 'machine_list.html', context)


def machine_add_form(request):
	if request.method == 'POST':
		machine = AddMachineForm(request.POST or None)
		if machine.is_valid():
			machine.save()
	else:
		machine = AddMachineForm()
	context = {'machine': machine}
	return render(request, 'machine_add.html',context)

def machine_remove(request, id):
	post = Machine.objects.get(id=id)
	post.delete()
	return redirect('machines')
	return render(request, 'machine_remove.html')

		




def personnelle_list_view(request) :
	nb_personnelles = Personnelle.objects.count()
	personnelles = Personnelle.objects.all()
	context={
		'nb_personnelles' : nb_personnelles,
		'personnelles': personnelles
		}
	return render(request, 'personnelle_list.html', context)


def personnelle_add_form(request):
	if request.method == 'POST':
		personnelle = AddPersonnelleForm(request.POST or None)
		if personnelle.is_valid():
			personnelle.save()
	else:
		personnelle = AddPersonnelleForm()
	context = {'personnelle': personnelle}
	return render(request, 'personnelle_add.html',context)

def personnelle_remove(request, id):
	post = Personnelle.objects.get(id=id)
	post.delete()
	return redirect('personnelles')
	return render(request, 'personnelle_remove.html')




def infrastructure_list_view(request):
	nb_infrastrutures = Infrastructure.objects.count()
	infrastructures = Infrastructure.objects.all()
	context={
		'nb_infrastructures' : nb_infrastrutures,
		'infrastructures': infrastructures
		}
	return render(request, 'infrastructure_list.html', context)


def infrastructure_add_form(request):
	if request.method == 'POST':
		infrastructure = AddInfrastructureForm(request.POST or None)
		if infrastructure.is_valid():
			infrastructure.save()
	else:
		infrastructure = AddInfrastructureForm()
	context = {'infrastructure': infrastructure}
	return render(request, 'infrastructure_add.html',context)

def infrastructure_remove(request, id):
	post = Infrastructure.objects.get(id=id)
	post.delete()
	return redirect('infrastructures')
	return render(request, 'infrastructure_remove.html')