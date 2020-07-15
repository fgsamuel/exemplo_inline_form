from django import forms

from ex_inline_form.models import Cliente, Telefone


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'
