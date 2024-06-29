from django.shortcuts import render
from core.models import FeriadoModel
from datetime import date

def feriados(request):
    hoje = date.today()
    feriado_encontrado = FeriadoModel.objects.filter(data=hoje)
    if len(feriado_encontrado) == 0:
        return render(request, 'feriados.html')
    contexto = {'feriado':str(feriado_encontrado[0])}
    return render(request, 'feriados.html', contexto)