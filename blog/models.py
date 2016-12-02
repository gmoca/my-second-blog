from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Article(models.Model):
    # title = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, unique=True, verbose_name='titulo')
    slug = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    owner = models.ForeignKey(User, related_name='article_owner')
    tags = models.ManyToManyField(Tag, related_name='article_tag')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def get_string_tags(self):
        return ', '.join([tag.name for tag in self.tags.all()])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog.article_detail', kwargs={'slug': self.slug})
