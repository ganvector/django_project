from django.shortcuts import render

postagens = [
    {
        'autor': 'Vitor Nascimento',
        'titulo': 'Blog Post 1',
        'conteudo': 'Conteudo do primeiro post',
        'data_postagem': '4 de outubro de 2018'
    },
    {
        'autor': 'Ninguem',
        'titulo': 'Blog Post 2',
        'conteudo': 'Conteudo do segundo post',
        'data_postagem': '5 de outubro de 2018'
    },
]

def home(request):
    context = {
        'posts': postagens
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')