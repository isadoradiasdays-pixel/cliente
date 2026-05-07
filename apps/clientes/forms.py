from .models import cliente
from django import forms 


class clienteForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    nascimento = forms.CharField(widget=forms.DateInput(attrs={"class": "form-control", "type":"date"}))


    class Meta:
        model = cliente 
        fields = "__all__" 
        