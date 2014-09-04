from django.conf import settings
from django.conf.urls.static import static
import os.path
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()


site_media_root = os.path.join(os.path.dirname(__file__), "../media")

urlpatterns = patterns('',
    # Examples:
    url(r'^$',
     TemplateView.as_view(template_name="brownfieldapp/visrecon.html")),
    url(r'^visual_reconnaissance/',
     TemplateView.as_view(template_name="brownfieldapp/visrecon.html")),
    url(r'^menu/',
     TemplateView.as_view(template_name="brownfieldapp/menu.html")),
    # url(r'^$', 'brownfieldapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$',
    'django.views.static.serve', {'document_root': site_media_root}),
)
