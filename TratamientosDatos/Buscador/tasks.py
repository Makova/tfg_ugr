from __future__ import absolute_import, unicode_literals
from celery.task import Task
from celery import Celery
app = Celery('BuscadorBDMedical''BuscadorBDMedical', backend='redis://192.168.56.102:6379/0', broker='amqp://invitado:invitado@192.168.56.102//')
import urllib
import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

@app.task(bind=True)
def obtenerJson(self,url):
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    return data
