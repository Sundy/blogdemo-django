from django.contrib import admin
from blog.models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Keyword)
