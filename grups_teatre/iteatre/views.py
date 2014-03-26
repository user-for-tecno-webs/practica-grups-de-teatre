# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from iteatre.models import *
import json
from django.core.serializers.json import DjangoJSONEncoder

def ajuntamentspage(request):
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

def ajuntamentpage(request, ajuntamentid):
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

def grupsdeteatrepage(request):
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

def grupdeteatrepage(request, grupId):
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
	
def alumnatpage(request):
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

def alumnaepage(request, alumnaeId):
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

def ajuntamentsjsonpage(request, tipus, id):
	try:
		if tipus=='json':
			ajuntaments = Ajuntament.objects.all()
			list_ajuntaments = []
	        for a in ajuntaments:
		    	ajuntament = {"id": a.id, "nom": a.nom}
		    	list_ajuntaments.append(ajuntament)
			ajuntaments = json.dumps({"ajuntaments": list_ajuntaments}, cls=DjangoJSONEncoder)
			variables = Context({
		    		'ajuntaments.id': ajuntaments.get("id")
					'ajuntaments.nom': ajuntaments.get("nom")
					'ajuntaments.cif': ajuntaments.get("cif")
				})
		# else: cas per a XML	
	except:
		raise Http404('Error al generar la pagina.')

	template = get_template('ajuntamentsjsonpage.html')
	

	variables = Context({
		'ajuntaments': ajuntaments
		})
	"""
	
	"""	
	output = template.render(variables)
	return HttpResponse(output, mimetype="aplicationjson")

def grupsdeteatrejsonpage(request):
	try:
		grups = GrupTeatre.objects.all()
	except:
		raise Http404('Error al generar la pagina.')

	template = get_template('grupsdeteatrejsonpage.html')
	
	list_grups = []
	for g in grups:
		grup = {"nom": g.nom, "data comencament": g.data_comencament}
		list_grups.append(grup)
	grups = json.dumps({"grups de teatre": list_grups}, indent=4, cls=DjangoJSONEncoder)
	variables = Context({
		'grupsdeteatre': grups
		})
	output = template.render(variables)
	return HttpResponse(output, mimetype="aplicationjson")

def alumnatjsonpage(request):
	try:
		alumnat = Alumnat.objects.all()
	except:
		raise Http404('Error al generar la pagina.')

	template = get_template('alumnatjsonpage.html')
	
	list_alumnat = []
	for al in alumnat:
		alumnae = {"nom": al.nom, "Tel. personal": al.telefon_personal}
		list_alumnat.append(alumnae)
	alumnat = json.dumps({"alumnat": list_alumnat}, indent=4, cls=DjangoJSONEncoder)
	variables = Context({
		'alumnat': alumnat
		})
	output = template.render(variables)
	return HttpResponse(output, mimetype="aplicationjson")