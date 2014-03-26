# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from iteatre.models import *
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import simplejson

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


def one_Ajuntaments_json_page(request, tipus, idAjuntament):
	try:
		if tipus=='json':
			a = Ajuntament.objects.get(id = int(idAjuntament))
			list_ajuntaments = []
			ajuntament = {"id": a.id, "nom": a.nom}
			list_ajuntaments.append(ajuntament)
			result_json = {"Ajuntament":list_ajuntaments}
	except:
		raise Http404('Error al generar la pagina')

	return HttpResponse(json.dumps(result_json))


def all_Ajuntaments_json_page(request, tipus):
	try:
		if tipus=='json':
			ajuntaments = Ajuntament.objects.all()
			list_ajuntaments = []
	        for a in ajuntaments:
		    	ajuntament = {"id": a.id, "nom": a.nom}
		    	list_ajuntaments.append(ajuntament)
			ajuntaments = {"Ajuntaments": list_ajuntaments}

	except:
		raise Http404('Error al generar la pagina')

	return HttpResponse(json.dumps(ajuntaments))

def all_grup_de_teatre_json_page(request, tipus):
	try:
		if tipus=='json':
			grups_teatre = GrupTeatre.objects.all()
			list_grups = []
	        for grup in grups_teatre:
		    	grup_teatre = {"id": grup.id, "nom": grup.nom}
		    	list_grups.append(grup_teatre)
			grup_teatre_json = {"Grups Teatre": list_grups}

	except:
		raise Http404('Error al generar la pagina')

	return HttpResponse(json.dumps(grup_teatre_json))

def one_grup_de_teatre_json_page(request, tipus, idGrupTeatre):
	try:
		if tipus=='json':
			grup = GrupTeatre.objects.get(id = int(idGrupTeatre))
			list_grups = []
			grup_teatre = {"id": grup.id, "nom": grup.nom}
			list_grups.append(grup_teatre)
			grup_teatre_json = {"Grups Teatre": list_grups}

	except:
		raise Http404('Error al generar la pagina')

	return HttpResponse(json.dumps(grup_teatre_json))

def all_alumnat_json_page(request, tipus):
	try:
		if tipus=='json':
			alumnat = Alumnat.objects.all()
			list_alumnat = []
	        for al in alumnat:
		    	alumnae = {"nom": al.nom, "Tel. personal": al.telefon_personal}
		    	list_alumnat.append(alumnae)
			alumnae_json = {"Alumnat": list_alumnat}

	except:
		raise Http404('Error al generar la pagina')

	return HttpResponse(json.dumps(alumnae_json))

def alumnae_json_page(request, tipus, idAlumne):
	try:
		if tipus=='json':
			al = Alumnat.objects.get(id = int(idAlumne))
			list_alumnat = []
			alumnae = {"nom": al.nom, "Tel. personal": al.telefon_personal}
			list_alumnat.append(alumnae)
			alumnae_json = {"Alumne/a": list_alumnat}

	except:
		raise Http404('Error al generar la pagina')

	return HttpResponse(json.dumps(alumnae_json))




