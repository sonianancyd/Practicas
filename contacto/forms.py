from django import forms

class Formulario(forms.Form):
    asunto=forms.CharField()
    nombre=forms.CharField()
    mail=forms.EmailField()
    departamento=forms.CharField()
    num_cliente=forms.IntegerField(required=False)
    consulta=forms.ChoiceField(choices=[("ventas","Departamento de Ventas"),("soporte", "Soporte")])
    
