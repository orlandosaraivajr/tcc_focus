from django.shortcuts import render
from core.models import FeriadoModel
from datetime import date

def feriados(request):
    contexto = {}
    feriado_encontrado = FeriadoModel.objects.filter(data=date.today())
    if len(feriado_encontrado) == 1:
        contexto = {'feriado':str(feriado_encontrado[0])}
    return render(request, 'feriados.html', contexto)