from django.shortcuts import render
from .models import Prestamo
def inicio(request):
    return render(request, "index.html")
# Create your views here.
from django.shortcuts import render
from .models import Prestamo

def inicio(request):
    prestamos = Prestamo.objects.all()
    print(Prestamo)
    return render(request, "index.html", {"prestamos": prestamos})

def create_task(request):
    prestamo = Prestamo(
        nombre=request.POST["nombre"],
        apellido=request.POST["apellido"],
        telefono=request.POST["telefono"],
        direccion=request.POST["direccion"],
        libro=request.POST["libro"],
        entregado=request.POST["entregado"],
        
    )
    prestamo.save()
    return redirect("/dispensario/")