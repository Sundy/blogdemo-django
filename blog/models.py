from django.db import models

# Create your models here.

class Author(models.Model):
	author_name = models.CharField(max_length=30)

class Category(models.Model):
	cate_name = models.CharField(max_length = 30)


class Keyword(models.Model):
	key_name = models.CharField(max_length = 30)


class Article(models.Model):
	article_name = models.CharField(max_length = 200)
	#article_content = models.TextField()
	article_date = models.DateField()
	comment_count = models.IntegerField()
	artist = models.ForeignKey(Author)
	cate = models.ForeignKey(Category)
	keywords = models.ManyToManyField(Keyword)




