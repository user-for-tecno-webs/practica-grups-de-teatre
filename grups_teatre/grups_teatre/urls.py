from django.conf.urls import patterns, include, url

from iteatre import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'grups_teatre.views.home', name='home'),
    # url(r'^grups_teatre/', include('grups_teatre.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajuntaments/$', views.ajuntamentspage, name='ajuntamentspage'),
    url(r'^grupsdeteatre/$', views.grupsdeteatrepage, name='grupsdeteatrepage'),
    url(r'^alumnat/$', views.alumnatpage, name='alumnatpage'),

    url(r'^ajuntaments/(\d{1,2})/$', views.ajuntamentpage, name='ajuntamentspage'),
    url(r'^grupsdeteatre/(\d{1,2})/$', views.grupdeteatrepage, name='grupdeteatrepage'),
    url(r'^alumnat/(\d{1,2})/$', views.alumnaepage, name='alumnaepage'),
    
    url(r'^json/ajuntaments/$', views.ajuntamentsjsonpage, name='ajuntamentsjsonpage'),
    url(r'^json/grupsdeteatre/$', views.grupsdeteatrejsonpage, name='grupsdeteatrejsonpage'),
    url(r'^json/alumnat/$', views.alumnatjsonpage, name='alumnatjsonpage'),
    url(r'^(\w+)/ajuntaments/(\d{1,2})/$', views.ajuntamentjsonpage, name='ajuntamentjsonpage'),
    # url(r'^(\w+)/grupsdeteatre/(\d{1,2})/$', views.grupdeteatrejsonpage, name='grupdeteatrejsonpage'),
	# url(r'^(\w+)/alumnat/(\d{1,2})/$', views.alumnaejsonpage, name='alumnaejsonpage'),
)
