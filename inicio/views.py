from django.shortcuts import render


def inicio(request):
    return render(request, 'inicio/index.html')

def proyecto_arriendo(request):
    return render(request, 'inicio/proyecto_arriendo.html')