from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.article_list_view, name='blog.article_list'),
    url(r'^$', views.ArticleListView.as_view(), name='blog.article_list'),
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='blog.article_detail'),
]