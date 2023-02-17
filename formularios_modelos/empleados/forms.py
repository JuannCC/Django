from django.forms import ModelForm
from .models import Empleados

class EmpleadosForm(ModelForm):
    class Meta:
        model= Empleados
        fields= '__all__'
        #exclude= ('email',)
        #extra_fields=['salary']
    