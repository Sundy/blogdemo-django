from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogdemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', 'blog.views.blog_list'),
    url(r'^blog/(?P<param>\d+)/$', 'blog.views.blog_show'),
    url(r'^media_root/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)
