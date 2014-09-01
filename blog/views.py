#-*- coding:utf-8 -*-
import blogdemo.settings
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def blog_list(request):
	static_url = blogdemo.settings.STATIC_URL
	web_domain = 'http://localhost:8000/blogdemo'#blogdemo.settings.WEB_DOMAIN
	return render_to_response('blog_list.html', locals())