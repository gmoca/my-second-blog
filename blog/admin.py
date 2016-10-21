from django.contrib import admin
from .models import Article, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'create_at', 'update_at', 'get_string_tags',)
    filter_horizontal = ('tags',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
