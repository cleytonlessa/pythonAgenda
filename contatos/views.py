from django.shortcuts import render
from . models import Contato
import pandas as pd
import numpy as np
import plotly.express as px
import wbgapi as wb


def index(request):
    contatos = Contato.objects.all()

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
