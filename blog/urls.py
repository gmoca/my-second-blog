from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.article_list_view, name='blog.article_list'),
    url(r'^$', views.ArticleListView.as_view(), name='blog.article_list'),
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='blog.article_detail'),
    url(r'^crear/$', views.ArticleCreateView.as_view(), name='blog.crear'),
    url(r'^editar/(?P<slug>[-\w]+)/$', views.ArticleUpdateView.as_view(), name='blog.editar'),
    url(r'^eliminar/(?P<slug>[-\w]+)/$', views.ArticleDeleteView.as_view(), name='blog.eliminar'),
]