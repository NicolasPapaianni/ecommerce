from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def saludo(request):                # esto es una view que devuelve un comentario
    return HttpResponse('Holis, segunda clase con django')

def segundo_template(request):      #esto es una view que devuelve un template
        today = datetime.now().date         
        context =  {                    # esto seria un diccionario y es la forma de pasarle datos al Front
            'name': 'Nico',
            'last_name': 'Papaianni',
            'today': today
        }
                        
        return render(request, 'template_2.html', context=context)

## otrooo

def template_con_lista(request):
    context={
        'lista': ['tomate','naranja', 'banana']
    }
    return render(request, 'template_lista.html', context=context)


