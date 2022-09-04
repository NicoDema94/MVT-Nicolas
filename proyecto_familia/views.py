from django.http import HttpResponse
from django.template import Template, Context, loader
from app_familia.models import Familia

def datos(request):
    queryset=Familia.objects.all()
    diccionario = {'miembros': queryset}
    plantilla = loader.get_template('familia.html')
    base=plantilla.render(diccionario)

    return HttpResponse(base)