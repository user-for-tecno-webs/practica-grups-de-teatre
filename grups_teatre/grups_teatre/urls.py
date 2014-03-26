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
    
    url(r'^ajuntaments/$', views.ajuntaments_page, name='ajuntamentspage'),
    url(r'^ajuntaments/(\d{1,2})/$', views.ajuntament_page, name='ajuntamentspage'),
    url(r'^(\w+)/ajuntaments/$', views.all_Ajuntaments_json_page, name='ajuntaments_json_page'),
    url(r'^(\w+)/ajuntaments/(\d{1,2})/$', views.one_Ajuntaments_json_page, name='ajuntaments_json_page'),

    url(r'^grupsdeteatre/$', views.grups_de_teatre_page, name='grupsdeteatrepage'),
    url(r'^grupsdeteatre/(\d{1,2})/$', views.grup_de_teatre_page, name='grupdeteatrepage'),
    url(r'^(\w+)/grupsdeteatre/$', views.all_grup_de_teatre_json_page, name='grupsdeteatrejsonpage'),
    url(r'^(\w+)/grupsdeteatre/(\d{1,2})$', views.one_grup_de_teatre_json_page, name='grupsdeteatrejsonpage'),

    url(r'^alumnat/$', views.alumnat_page, name='alumnatpage'),
    url(r'^alumnat/(\d{1,2})/$', views.alumnae_page, name='alumnaepage'),
    url(r'^(\w+)/alumnat/$', views.all_alumnat_jx_page, name='alumnatjsonpage'),
    url(r'^(\w+)/alumnat/(\d{1,2})/$', views.alumnae_jx_page, name='alumnaejsonpage'),	
)







