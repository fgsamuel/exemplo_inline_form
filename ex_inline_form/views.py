from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from ex_inline_form.forms import ClienteForm, TelefoneForm
from ex_inline_form.models import Cliente, Telefone


def lista(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        context = {
            'lista': clientes,
        }
        return render(request, "ex_inline_form/lista.html", context)


def inserir(request):
    if request.method == "GET":
        form = ClienteForm()
        form_telefone_factory = inlineformset_factory(Cliente, Telefone, form=TelefoneForm, extra=3)
        form_telefone = form_telefone_factory()
        context = {
            'form': form,
            'form_telefone': form_telefone,
        }
        return render(request, "ex_inline_form/form.html", context)
    elif request.method == "POST":
        form = ClienteForm(request.POST)
        form_telefone_factory = inlineformset_factory(Cliente, Telefone, form=TelefoneForm)
        form_telefone = form_telefone_factory(request.POST)
        if form.is_valid() and form_telefone.is_valid():
            cliente = form.save()
            form_telefone.instance = cliente
            form_telefone.save()
            return redirect(reverse('inlineform_lista'))
        else:
            context = {
                'form': form,
                'form_telefone': form_telefone,
            }
            return render(request, "ex_inline_form/form.html", context)


def editar(request, cliente_id):
    if request.method == "GET":
        objeto = Cliente.objects.filter(id=cliente_id).first()
        if objeto is None:
            return redirect(reverse('inlineform_lista'))
        form = ClienteForm(instance=objeto)
        form_telefone_factory = inlineformset_factory(Cliente, Telefone, form=TelefoneForm, extra=3)
        form_telefone = form_telefone_factory(instance=objeto)
        context = {
            'form': form,
            'form_telefone': form_telefone,
        }
        return render(request, "ex_inline_form/form.html", context)
    elif request.method == "POST":
        objeto = Cliente.objects.filter(id=cliente_id).first()
        if objeto is None:
            return redirect(reverse('inlineform_lista'))
        form = ClienteForm(request.POST, instance=objeto)
        form_telefone_factory = inlineformset_factory(Cliente, Telefone, form=TelefoneForm)
        form_telefone = form_telefone_factory(request.POST, instance=objeto)
        if form.is_valid() and form_telefone.is_valid():
            cliente = form.save()
            form_telefone.instance = cliente
            form_telefone.save()
            return redirect(reverse('inlineform_lista'))
        else:
            context = {
                'form': form,
                'form_telefone': form_telefone,
            }
            return render(request, "ex_inline_form/form.html", context)
