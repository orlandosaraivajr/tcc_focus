from django.shortcuts import render

def feriados(request):
    return render(request, 'feriados.html')