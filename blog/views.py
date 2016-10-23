# from django.shortcuts import render
from .models import Article
from django.views import generic
# Create your views here.


# def article_list_view(generic.ListView):
class ArticleListView(generic.ListView):
    paginate_by = 2
    ordering = '-create_at'
    template_model = 'blog/article_list.html'
    model = Article
    context_object_name = 'articles'


class ArticleDetailView(generic.DetailView):
    template_model = 'blog/article_detail.html'
    model = Article
    context_object_name = 'article'

