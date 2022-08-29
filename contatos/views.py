from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

from . models import Contato
import pandas as pd
import numpy as np
import plotly.express as px
import wbgapi as wb


def index(request):
    # contatos = Contato.objects.all()
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )

    """
    desemprego = wb.data.DataFrame('SL.UEM.TOTL.ZS', economy=[
                                   'BRA', 'ARG', 'MEX'], time=range(2016, 2021))
    lista_paises = np.array([desemprego.index])
    desemprego = desemprego.melt(var_name='Ano', value_name='Desemprego')
    desemprego['País'] = np.resize(lista_paises, len(desemprego))
    desemprego['Ano'] = pd.to_numeric(desemprego['Ano'].str.slice(start=2))

    import plotly.express as px

    fig = px.bar(
    desemprego,
    x='País',
    y=['Desemprego'],
    color='País',
    animation_frame='Ano',
    animation_group='País',
    range_y=[0,14],
    title='Desemprego America Latina 2010 - 2020',
    template='plotly_dark'
    )
    fig.show()

    teste = "cleyton"
    """

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR,
                             'Campo termo não pode ficar vazio')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

#    contatos = Contato.objects.order_by('-id').filter(
#        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
#        mostrar=True
#    )
#    print(contatos.query)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
