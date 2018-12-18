from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def helloworld(request):
    return HttpResponse("Hello dr Chandra :)")


def hello2(request, name):
    return HttpResponse("Hello {0}".format(name))


def maths(request, function, param1, param2):
    if function == 'add':
        out = param1 + param2
    elif function == 'sub':
        out = param1 - param2
    else:
        out = "Brak lub błedne dane wejsciowe"

    return HttpResponse(out)
