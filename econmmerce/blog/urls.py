from django.urls import path
from blog.views import create_article, List_articles


urlpatterns = [
    path('create-article/', create_article, name = 'create_article'),
    path('list-articles/', List_articles.as_view(), name = 'list_articles'), #AL usar clas agregamos el .as_view
]