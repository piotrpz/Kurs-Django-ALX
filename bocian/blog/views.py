from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context,loader

from .models import Wpis


# Create your views here.

def index(request):
    obiects = Wpis.objects.all()
    lista = []
    for obiect in obiects:
        title = obiect.tytul
        lista.append(title)

    return HttpResponse(lista)


def index_temp(request):
    # t = Template('tu wstawiasz zmioenna do template {{ zmienna }}')

    #t = loader.get_template('blog/index.html')
    #context = {'zmienna': '2.45'}
    # wynik = t.render(context)
    # return HttpResponse(wynik)
    return render(request=request,
                  template_name='blog/index.html')
