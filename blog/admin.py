from django.contrib import admin
from blog.models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'get_category', 'comment_count', 'get_authorname', 'article_date')
    list_editable = ('article_date',)
    list_filter = ('article_date', 'artist__author_name')
    search_fields = ('article_name',)
    ordering = ('article_date','comment_count')


class AuthorAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class KeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article,ArticleAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Keyword,KeywordAdmin)
