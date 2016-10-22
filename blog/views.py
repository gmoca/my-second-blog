from django.shortcuts import render
from .models import Article
# Create your views here.


def article_list_view(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    print(context)
    return render(request, 'blog/article_list.html', context)
