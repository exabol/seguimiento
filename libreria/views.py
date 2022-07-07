from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Ilcs
from .models import Departamentos
from .forms import IlcForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def ilcs(request):
    ilcs = Ilcs.objects.all()
    return render(request, 'ilcs/index.html', {'ilcs': ilcs} )

def crear(request):
    formulario = IlcForm(request.POST or None)
    return render(request, 'ilcs/crear.html', {'formulario': formulario})

def editar(request):
    return render(request, 'ilcs/editar.html')