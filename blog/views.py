# from django.shortcuts import render
from contextlib import _GeneratorContextManager
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from .models import Article
from django.views import generic
from django.conf import settings
from .forms import ArticleCreateForm
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

class ArticleCreateView(generic.CreateView):
    template_name = 'blog/article_form.html'
    model = Article
    form_class = ArticleCreateForm
    # fields = ('title', 'body')

    def get_context_data(self, **kwargs):
        # obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear articulo'
        context['nombre_btn'] = 'Crear'
        return context

    def dispatch(self, request, *args, **kwargs):
        # Nota: Dejo para el lector como ejercicio que cambie este
        # comportamiento, actualmente, solo comprueba si es usuario
        # tiene permisos para añadir un articulo, si no lo tiene, lo
        # redirecciona a login, pero, ¿y si esta logueado y simplemente
        # no tiene permisos?
        # El compportamiento logico seria:
        # ¿Estas logueado?
        # ¿Tiene permisos?
        # Continuar con la ejecución
        # ¿No tienes permisos?
        # Redireccionar a una pagina informando que no tiene permisos
        # para añadir un articulo.
        # Si no estas logueado:
        # Redireccionar a pagina de login

        if not request.user.has_perms('blog.add_article'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(generic.UpdateView):
    template_name = 'blog/article_form.html'
    model = Article
    form_class = ArticleCreateForm

    def dispatch(self, request, *args, **kwargs):
        # Al igual que con ArticleCreateView, dejo al lector
        # que cambie el comportamiento de este método para saber
        # si esta logueado y tiene permisos.
        # Ver el comentario de ArticleCreateView en el método
        # dispatch
        if not request.user.has_perms('blog.change_article'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        # Añadimos nuevas variables de contexto al diccionario
        context['title'] = 'Editar articulo'
        context['nombre_btn'] = 'Editar'
        # Devolvemos el contexto
        return context

class ArticleDeleteView(generic.DeleteView):
    template_name = 'blog/confirmar_eliminacion.html'
    success_url = reverse_lazy('blog.article_list')
    model = Article

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('blog.delete_article'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)
