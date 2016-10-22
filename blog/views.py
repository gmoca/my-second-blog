# from django.shortcuts import render
from .models import Article
from django.views import generic
# Create your views here.


# def article_list_view(generic.ListView):
class ArticleListView(generic.ListView):
    template_model = 'bloc/article_list.html'
    model = Article
    context_object_name = 'articles'