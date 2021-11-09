from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
#  from django.http import Http404


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
    contatos = Contato.objects.order_by('-id').filter(nome__icontains=termo,
     sobrenome__icontains=termo,
     publicar=True)
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
