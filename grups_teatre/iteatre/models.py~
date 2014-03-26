from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ajuntament(models.Model):
	nom = models.CharField(max_length=50)
	telefon = models.PositiveIntegerField()
	email = models.EmailField()
	adreca = models.CharField(max_length=60)
	cif = models.CharField(max_length=9)
	def __unicode__(self):
		return self.nom


class GrupTeatre(models.Model):
	nom = models.CharField(max_length=50)
	data_comencament = models.DateField()
	data_finalitzacio = models.DateField()
	dies_i_horaris = models.CharField(max_length=60)
	user = models.ForeignKey(User)
	ajuntament = models.ForeignKey(Ajuntament)
	def __unicode__(self):
		return self.nom
	
class Alumnat(models.Model):
	nom = models.CharField(max_length=50)
	telefon_personal = models.PositiveIntegerField()
	telefon_persona_encarregada = models.PositiveIntegerField()
	email = models.EmailField()
	nif_nie = models.CharField(max_length=8)
	compte_bancari = models.CharField(max_length=24)
	data_naixement = models.DateField()
	curs = models.CharField(max_length=15)
	sexe = models.CharField(max_length=15)
	pais = models.CharField(max_length=30)
	grup_teatre = models.ForeignKey(GrupTeatre)
	def __unicode__(self):
		return self.nom

""" --- utilitzarem class User builtin en Django, considerant que Professorat i Funcionari gestionaran la info. des de
        la pagina de administracio de django ----

class Professorat(models.Model):
	nom = models.CharField()
	telefon = models.PositiveIntegerField()
	email = models.EmailField()
	nif_nie = models.CharField()
	dataNaixement = models.DateField()
	titulacio = models.TextField(max_length=300)

class Funcionari(models.Model):
	nom = models.CharField()
	telefondirecte = models.PositiveIntegerField()
	emailpersonalajuntament = models.EmailField()
"""
