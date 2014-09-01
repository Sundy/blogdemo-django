#-*- coding:utf-8 -*-
import blogdemo.settings
from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import *

# Create your views here.

def blog_list(request):
	
	articles = Article.objects.all() 

	return render_to_response('blog_list.html', locals())

def blog_show(request, param):
	
	article = Article.objects.get(id = param) 

	return render_to_response('blog_show.html', locals())