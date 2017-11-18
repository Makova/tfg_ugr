from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import Context
from django.http import JsonResponse
from django.core import serializers
import json
import requests
import urllib
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import os
import threading

data_array={}
palabra_clave=""
def obtenerJson(url,tipo):
	response = urlopen(url)
	data = json.loads(response.read().decode('utf-8'))
	if(tipo=="array"):
		data_array=data
		print(data_array)
	return data
def buscar(request):
	if request.method == "POST":
		palabra_clave=request.POST['search']
		url_ncbi = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={}&reldate=60&datetype=edat&retmax=10&usehistory=y&retmode=json'.format(palabra_clave)
		url_array = 'https://www.ebi.ac.uk/arrayexpress/json/v3/experiments?keywords={}&species="homo%20sapiens"'.format(palabra_clave)
		data_ncbi=obtenerJson(url_ncbi,"ncbi")
		hebra_array = threading.Thread(target=obtenerJson, args=(url_array,"array",))
		hebra_array.start()
		for elemento in data_ncbi['esearchresult'].items():
			print(elemento)
		print(data_array)
		return index(request)
	else:
		return index(request)


#def busqueda_avanzada(palabra_clave, tecnologia_secuenciacion,localizacion, organismo, base_datos):
#	if (base_datos=="ncbi"):




def devuelve_status(request):
	opcional={ "status": "OK"}
	return  JsonResponse(opcional, safe=False)

def probando_REST(request):
	if request.method == 'GET':
		url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=cancer&reldate=60&datetype=edat&retmax=10&usehistory=y&retmode=json'
		response = urlopen(url)
		data = json.loads(response.read().decode('utf-8'))
		return JsonResponse(data, safe=False)
	elif request.method == 'POST':
		opcional={ "status": "OK", "ejemplo ": { "ruta": os.path.dirname(os.path.abspath(__file__)), "valor": "{JSON: devuelto}"}}
		return  JsonResponse(opcional, safe=False)


def index(request):
	return render(request, 'index.html')
