from django import template
from ..models import Article, Tag


register = template.Library()
@register.inclusion_tag('blog/_menus.html')
def get_menus_blog():
    context = {
        # Obtener lista completa de etiquetas
        'lista_tags': Tag.objects.all(),
        # Obtener las 5 ultimas entradas
        'ultimos_articulos': Article.objects.order_by('-create_at')[:5]
    }
    return context


@register.filter(name='read_more')
def read_more(article):
    pattern = '<!-- read_more -->'
    body = article.body
    if pattern in body:
        pos = body.index(pattern)
        replace = '<a href="{}" class="small">Sigue leyendo...</a>'.format(
            article.get_absolute_url())
        body_return = body.replace(pattern, replace)
        return body_return[:pos + len(replace)]
    return body
