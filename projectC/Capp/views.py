
from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import DadosGerais
from django.core.paginator import Paginator
from . import models

# Create your views here.



def article(request):
    return render(request, 'home/article.html')

#################### HOME PAGES


def home(request):
    dados = DadosGerais.objects.all()
    if 'kic' in request.GET:
        id_pesquisa = request.GET['kic']
        try:
            id_pesquisa = int(id_pesquisa)
            dado = get_object_or_404(DadosGerais, kic=id_pesquisa)
            return redirect('pagina_objetos', kic=id_pesquisa)
        except ValueError:
            return render(request, 'notf.html')
    else:
        return render(request, 'home/home.html', {'dados': dados})

#def pagina_objetos(request, kic):
#    dado = get_object_or_404(DadosGerais, kic=kic)
#    template_name = f'mid/kic{kic}/page{kic}.html'
#    return render(request, template_name, {'dado': dado})


def figskic3228863(request):
    return render(request, 'mid/kic3228863/figs3228863.html')


#################### HOME PAGES END

def pagina_objetos(request, kic):
    # Obtenha todos os objetos relacionados ao 'kic'
    lista_de_dados = DadosGerais.objects.filter(kic=kic)

    # Número de itens por página
    itens_por_pagina = 12

    # Crie um objeto Paginator com a lista de dados e o número de itens por página
    paginator = Paginator(lista_de_dados, itens_por_pagina)

    # Obtenha o número da página da consulta de parâmetro GET (se não for fornecido, use 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template_name = f'mid/kic{kic}/page{kic}.html'
    return render(request, template_name, {'page_obj': page_obj})

def pagina_continuacao(request, kic):
    # Obtenha todos os objetos relacionados ao 'kic'
    lista_de_dados = DadosGerais.objects.filter(kic=kic)

    # Número total de objetos
    total_objetos = lista_de_dados.count()

    # Número de itens por página
    itens_por_pagina = 12

    # Calcule o número total de páginas necessárias para exibir os objetos em grupos de 12
    total_paginas = (total_objetos + itens_por_pagina - 1) // itens_por_pagina

    # Obtenha o número da página da consulta de parâmetro GET (se não for fornecido, use 1)
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)

    if page_number < 1:
        page_number = 1
    elif page_number > total_paginas:
        page_number = total_paginas

    # Calcule o índice inicial e final dos objetos a serem exibidos nesta página
    indice_inicial = (page_number - 1) * itens_por_pagina
    indice_final = min(indice_inicial + itens_por_pagina, total_objetos)

    # Obtenha a lista de objetos a serem exibidos nesta página
    lista_pagina = lista_de_dados[indice_inicial:indice_final]

    template_name = f'mid/kic{kic}/continuacao{kic}.html'
    return render(request, template_name, {
        'lista_pagina': lista_pagina,
        'total_paginas': total_paginas,
        'page_number': page_number,
    })

