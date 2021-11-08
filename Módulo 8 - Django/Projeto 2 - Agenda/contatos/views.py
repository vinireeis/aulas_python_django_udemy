from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Contato
from django.http import Http404


def index(request):
    contatos = Contato.objects.all()

    return render(request, 'contatos/index.html', {'contatos': contatos})


# def ver_contato(request, id_contato):
#     try:
#         contato = Contato.objects.get(id=id_contato)
#         return render(request, 'contatos/ver_contato.html', {
#             'contato': contato
#             })
#     except Contato.DoesNotExist as e:
#         raise Http404()


def ver_contato(request, id_contato):
    contato = get_object_or_404(Contato, id=id_contato)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
        })
