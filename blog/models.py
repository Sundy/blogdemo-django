from django.db import models
from django.utils.html import format_html

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=30)


class Category(models.Model):
    cate_name = models.CharField(max_length=30)


class Keyword(models.Model):
    key_name = models.CharField(max_length=30)


class Article(models.Model):
    article_name = models.CharField(max_length=200)
    # article_content = models.TextField()
    cate = models.ForeignKey(Category)
    article_date = models.DateField()
    comment_count = models.IntegerField()
    artist = models.ForeignKey(Author)
    keywords = models.ManyToManyField(Keyword)

    def get_authorname(self):
        return format_html('<a href="user/1">'+self.artist.author_name+'</a>')
    get_authorname.short_description = "Author Name"
    get_authorname.allow_tags = True

    def get_category(self):
        return self.cate.cate_name
    get_category.short_description = "Category"





