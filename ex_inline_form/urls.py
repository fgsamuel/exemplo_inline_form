from django.urls import path

from ex_inline_form.views import lista, inserir, editar

urlpatterns = [
    path('lista/', lista, name='inlineform_lista'),
    path('inserir/', inserir, name='inlineform_inserir'),
    path('editar/<int:cliente_id>/', editar, name='inlineform_editar'),
]
