from django import forms
from .models import Cliente, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'platos', 'fecha_entrega', 'hora_entrega', 'es_entrega_domicilio']
        widgets = {
            'platos': forms.CheckboxSelectMultiple
        }
