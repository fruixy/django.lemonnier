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
		form = AddMachineForm(request.POST or None)
		if form.is_valid():
			new_machine = Machine(
				nom=form.cleaned_data['nom']
				)
			new_machine.save()
			return redirect('machines')
	
	else:
		form = AddMachineForm()
		context = {'form': form}
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
		form = AddPersonnelleForm(request.POST or None)
		if form.is_valid():
			new_personnelle = Personnelle(nom=form.cleaned_data['nom'])
			new_personnelle.save()
			return redirect('personnelles')
	
	else:
		form = AddPersonnelleForm()
		context = {'form': form}
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
		form = AddInfrastructureForm(request.POST or None)
		if form.is_valid():
			new_infrastructure = Infrastructure(nom=form.cleaned_data['infrastructure'])
			new_infrastructure.save()
			return redirect('machines')
	
	else:
		form = AddInfrastructureForm()
		context = {'form': form}
		return render(request, 'infrastructure_add.html',context)