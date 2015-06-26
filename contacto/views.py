from django.shortcuts import render
from contacto.forms import Formulario

# Create your views here.
def mail(asunto, nombre, desde, para, cuerpo):
    print (asunto, nombre,desde, para,cuerpo)
    
def Contacto(request):
    form=Formulario()
	
    return render(request,'paginadeContacto.html', {'form': form, 'titulo': "Contactenos sr visitante:"})
            


"""
if resquest.method=="POST":
        form=Formulario(resquest.POST)
        if form.is_valid():
            mail(form.cleaned_data["asunto","nombre","desde","mail","para","consulta"])

"""
    
        

    
