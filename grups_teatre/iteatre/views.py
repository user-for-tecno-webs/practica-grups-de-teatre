# Create your views here.
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import loader, Context, Template
from iteatre.models import *
from django.utils import simplejson
from django.shortcuts import render_to_response
import json

def ajuntaments_page(request):
	try:
		ajuntaments = Ajuntament.objects.all()
	except:
		raise Http404('Error al generar la pagina.')

	template = get_template('ajuntamentspage.html')
	variables = Context({
		'ajuntaments': ajuntaments
		})
	output = template.render(variables)
	return HttpResponse(output)

def ajuntament_page(request, ajuntamentid):
	try:
		ajuntamentid = int(ajuntamentid)
		ajuntament = Ajuntament.objects.get(id=ajuntamentid)
	except:
		raise Http404('Error al generar la pagina.')

	template = get_template('ajuntamentpage.html')
	variables = Context({
		'ajuntament': ajuntament
		})
	output = template.render(variables)
	return HttpResponse(output)

def grups_de_teatre_page(request):
	try:
		grupsdeteatre = GrupTeatre.objects.all()
	except:
		raise Http404('Error al generar la pagina.')

	template = get_template('grupsdeteatrepage.html')
	variables = Context({
		'grupsdeteatre': grupsdeteatre
		})
	output = template.render(variables)
	return HttpResponse(output)

def grup_de_teatre_page(request, grupId):
	try:
		grupId = int(grupId)
		grupdeteatre = GrupTeatre.objects.get(id=grupId)
	except:
		raise Http404('Error al generar la pagina.')

	template = get_template('grupdeteatrepage.html')
	variables = Context({
		'grupdeteatre': grupdeteatre
		})
	output = template.render(variables)
	return HttpResponse(output)	
	
def alumnat_page(request):
	try:
		alumnat = Alumnat.objects.all()
	except:
		raise Http404('Error al generar la pagina.')

	template = get_template('alumnatpage.html')
	variables = Context({
		'alumnat': alumnat
		})
	output = template.render(variables)
	return HttpResponse(output)

def alumnae_page(request, alumnaeId):
	try:
		alumnaeId = int(alumnaeId)
		alumnae = Alumnat.objects.get(id=alumnaeId)
	except:
		raise Http404('Error al generar la pagina.')

	template = get_template('alumnaepage.html')
	variables = Context({
		'alumnae': alumnae
		})
	output = template.render(variables)
	return HttpResponse(output)


def one_ajuntament_jx_page(request, tipus, idAjuntament):
	try:
		a = Ajuntament.objects.get(id = int(idAjuntament))
		if tipus=='json':
			list_ajuntaments = []
			ajuntament = {"id": a.id, "nom": a.nom}
			list_ajuntaments.append(ajuntament)
			ajuntament_json = {"Ajuntament":list_ajuntaments}
			return HttpResponse(json.dumps(ajuntament_json))
		elif tipus=='xml':
			variables = Context({
						'ajuntament': a
						})
			t = loader.get_template('ajuntamentpage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")	
	except:
		raise Http404('Error al generar la pagina')

	


def all_ajuntaments_jx_page(request, tipus):
	try:
		ajuntaments = Ajuntament.objects.all()
		if tipus=='json':
			list_ajuntaments = []
	        for a in ajuntaments:
		    	ajuntament = {"id": a.id, "nom": a.nom}
		    	list_ajuntaments.append(ajuntament)
			ajuntaments = {"Ajuntaments": list_ajuntaments}
			return HttpResponse(json.dumps(ajuntaments))
		elif tipus=='xml':
			variables = Context({
						'ajuntaments': ajuntaments
						})
			t = loader.get_template('ajuntamentspage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")
	except:
		raise Http404('Error al generar la pagina')

	

def all_grups_de_teatre_jx_page(request, tipus):
	try:
		grups_teatre = GrupTeatre.objects.all()
		if tipus=='json':			
			list_grups = []
	        for grup in grups_teatre:
		    	grup_teatre = {"id": grup.id, "nom": grup.nom}
		    	list_grups.append(grup_teatre)
			grups_teatre_json = {"Grups Teatre": list_grups}
			return HttpResponse(json.dumps(grups_teatre_json))
		elif tipus=='xml':
			variables = Context({
						'grups': grups_teatre
						})
			t = loader.get_template('grupspage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")	
	except:
		raise Http404('Error al generar la pagina')

	

def grup_de_teatre_jx_page(request, tipus, idGrupTeatre):
	try:
		grup = GrupTeatre.objects.get(id = int(idGrupTeatre))
		if tipus=='json':			
			list_grups = []
			grup_teatre = {"id": grup.id, "nom": grup.nom}
			list_grups.append(grup_teatre)
			grup_teatre_json = {"Grup de Teatre": list_grups}
			return HttpResponse(json.dumps(grup_teatre_json))
		elif tipus=='xml':
			variables = Context({
						'grup': grup
						})
			t = loader.get_template('gruppage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")
	except:
		raise Http404('Error al generar la pagina')

	

def all_alumnat_jx_page(request, tipus):
	try:
		alumnat = Alumnat.objects.all()
		if tipus=='json':			
			list_alumnat = []
	        for al in alumnat:
		    	alumnae = {"nom": al.nom, "Tel. personal": al.telefon_personal}
		    	list_alumnat.append(alumnae)
			alumnat_json = {"Alumnat": list_alumnat}
			return HttpResponse(json.dumps(alumnat_json))
		elif tipus=='xml':
			variables = Context({
						'alumnat': alumnat
						})
			t = loader.get_template('alumnatpage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")		   		
	except:
		raise Http404('Error al generar la pagina')

	

def alumnae_jx_page(request, tipus, idAlumne):
	try:
		al = Alumnat.objects.get(id = int(idAlumne))	 
		if tipus=='json':
			list_alumnat = []
			alumnae = {"nom": al.nom, "Tel. personal": al.telefon_personal}
			list_alumnat.append(alumnae)
			alumnae_json = {"Alumne/a": list_alumnat}
			return HttpResponse(json.dumps(alumnae_json))
		elif tipus=='xml':		    
			variables = Context({
						'alumnae': al
						})
			t = loader.get_template('alumnaepage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")
	except:
		raise Http404('Error al generar la pagina')

	




