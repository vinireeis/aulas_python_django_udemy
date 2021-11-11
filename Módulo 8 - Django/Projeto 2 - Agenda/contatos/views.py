from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import Http404
from django.contrib import messages


def index(request):
    contatos = Contato.objects.order_by('-id').filter(publicar=True)
    paginator = Paginator(contatos, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'contatos/index.html', {'contatos': contacts})


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


def busca(request):
    termo = request.GET.get('termo')
    if termo is None:
        messages.add_message(request, messages.ERROR, 'Campo de busca não pode estar vazio')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {'contatos': contacts})
# def busca(request):
#     contatos = Contato.objects.order_by('-id').filter(publicar=True)
#     paginator = Paginator(contatos, 3)
#     page = request.GET.get('page')
#     contacts = paginator.get_page(page)
#     return render(request, 'contatos/busca.html', {'contatos': contacts})

#   contatos = Contato.objects.order_by('-id').filter(Q(nome__icontains=termo) | Q(sobrenome__icontains=termo)  >> buscando por dois termos, porém não concatena os termos.

# print(contatos.query) apresenta no terminal toda a query que está sendo executada para determinado objeto
