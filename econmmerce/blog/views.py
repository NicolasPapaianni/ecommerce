from msilib.schema import ListView
from django.shortcuts import render
from blog.models import Articles
from django.views.generic import ListView


class List_articles(ListView):
    model = Articles
    template_name = 'articles/list_articles.html'












def create_article(request):
    new_article = Articles.objects.create(
        title = 'El Bitcoin esta bajando',
        description = 'Esta bajando mucho, salgan o compren mas',
        author = 'Juan Ignasio Tessio'
        )
    context = { 'new_article' : new_article}
    return render(request, 'articles/new_article.html', context=context)
