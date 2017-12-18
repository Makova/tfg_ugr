# Buscador de datos médicos  
[![Build [![Build Status](https://travis-ci.org/AntonioAlcM/tfg_ugr.svg?branch=master)](https://travis-ci.org/AntonioAlcM/tfg_ugr) [![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]() [![license](https://www.gnu.org/graphics/lgplv3-88x31.png)](https://www.gnu.org/licenses/lgpl.html)
[![GitHub
Vamos a desarrollar una aplicación web, que haga una búsqueda múltiple en 3 bases de datos distintas.
Cada búsqueda contendrá, una palabra de búsqueda y un conjunto de filtros.    
Las búsquedas se mostraran en una lista, cuyos campos serán, descripción, base de datos en la que se encontró y enlace al objeto de la base de datos. Las búsquedas tendrán un sistema de filtrado.  

## Servicios y herramientas que se van a usar

Voy a usar una base de datos NoSQL, porque me interesa que sea escalable.  
Voy a usar Python y django para programar la aplicación.
Será desplegada en un servidor web en la nube.

## Testeo

En este proyecto vamos a utilizar la librería unittest, se ha elegido por su amplia gama de funcionalidades.

## Integración continua

Como sistema de integración continua he usado travis-ci, se ha elegido travis-ci por su fácil manejo, ademas permite instalar las dependencias requirements.txt de python de forma automática. Otra ventaja que nos aporta es la posibilidad de ejecutar los test de forma inmediata, cuando se añade nuevas funcionalidades a la clase que se esta testeando.

## Despliegue en PaaS  
Después de observar las distintas opciones Paas (Engine yard, Openshif, Google app engine, Heroku, Appfog, Azure, AWS y Cloudno.de), hemos decidido usar heroku, ya que es la que mas recursos nos ofrece, en su modo gratuito. Hay otras Paas que nos dan mas recursos pero están mas limitadas en el tiempo, nos interesa disponer de mas tiempo para probar las plataformas. Además otra ventaja de Heroku es que permite la integración continua con Travis

### Migración del proyecto de Django a Heroku
Para migrar el proyecto vamos a seguir los pasos de este [tutorial](https://devcenter.heroku.com/articles/django-app-configuration), que podemos encontrar en la documentación de Heroku.
1. Instalamos el gunicorn, sino lo tenemos instalado y lo metemos en el archivo requirements.txt
2. Creamos el archivo Procfile, este archivo se usa para declarar explícitamente los tipos de procesos y puntos de entrada de su aplicación
	El contenido del mismo será: "web: gunicorn BuscadorBDMedical.wsgi --log-file -"


### Creación proyecto Heroku
Hay dos opciones, la primera es creando el proyecto desde la web de Heroku, es un proceso bastante intuitivo y fácil. Y la que voy a explicar es usando los comandos del toolbelt que nos proporciona Heroku.
1. Primero nos logueamos
![imagen](https://github.com/AntonioAlcM/IV17-18-Autoevaluacion/blob/master/Tema3/Imagenes/ejercicio2.1.png?raw=true)
2. Creamos el proyecto en Heroku con el comando "heroku create buscadorbdmedical"  
![imagen](https://github.com/AntonioAlcM/IV17-18-Autoevaluacion/blob/master/Tema3/Imagenes/hito3.1.png?raw=true)
4. Deshabilitamos por ahora la configuración de los archivos estáticos "heroku config:set DISABLE_COLLECTSTATIC=0"  
5. Hacemos un git push heroku master para hacer el despliegue
![imagen](https://github.com/AntonioAlcM/IV17-18-Autoevaluacion/blob/master/Tema3/Imagenes/hito3.2.png?raw=true)
Para asegurar la versión de python que queremos ejecutar, deberemos crear un archivo llamado runtime.txt en el directorio raíz de nuestro proyecto, dicho archivo contendrá la versión de python que queremos ejecutar. No es obligatorio su inclusión, pero en nuestro caso como queremos que se ejecute en la versión 2.7 de python lo añadiremos.

### Despliegue desde Github de forma automática
Para desplegar la aplicación en github de forma automática y que además pase los test haremos:
1. Nos vamos a la pagina web de Heroku en personal apps seleccionamos la aplicación.
2. Nos vamos al menú Deploy.
3. En Deployment method seleccionamos GitHub, buscamos el nombre del repositorio y lo seleccionamos.
4. Activamos la opción Automatically deploys from, por defecto activara la versión de la rama maestra.
5. Activamos Wait for CI to pass before deploy.
Con estos pasos ya tenemos desplegada nuestra aplicación. Para desplegar la aplicación en github nos hemos basado en [este manual](https://devcenter.heroku.com/articles/github-integration).
![imagen](https://github.com/AntonioAlcM/IV17-18-Autoevaluacion/blob/master/Tema3/Imagenes/hito3.3.png?raw=true)

### Observaciones
Es importante configurar el archivo settings para poder desplegar correctamente la aplicación. Para ello vamos a seguir la [guía](https://devcenter.heroku.com/articles/django-app-configuration) de Heroku.
Hay tres direcciones dentro de la aplicación web:
1. Probar el JSON status  
Despliegue https://buscadorbdmedical.herokuapp.com/status
2. Probar el JSON status mas el campo ejemplo  
[Enlace a la página ejemplo](https://buscadorbdmedical.herokuapp.com/buscador/ejemplo/)
3. Probar la aplicación REST  
[Enlace a la página para probar REST](https://buscadorbdmedical.herokuapp.com/buscador/rest/)

## Despliegue en DockerHub y Zeit  
Para poder crear un contenedor de Docker de forma automática, lo primero que debemos hacer es crear un Dockerfile en el directorio raíz de nuestro repositorio y configurarlo utilizando los comandos  que viene explicados en la documentación. En dicho Dockerfile elegiremos la imagen de sistema operativo que queremos instalar en el contenedor, los comandos que deseamos ejecutar una vez instalado el sistema operativo, además de descargar nuestro repositorio en el contendedor. En mi caso añadiré una línea en el Dockerfile, para que despliegue la aplicación

### Despliegue en DockerHub
Para almacenar en DockerHub el contenedor que hemos definido en nuestro repositorio de github, lo que debemos hacer es irnos al menú create y elegimos la opción create automated build, seleccionamos github y le pasamos el repositorio que tiene el Dockerfile.
![imagen](https://github.com/AntonioAlcM/IV17-18-Autoevaluacion/blob/master/Tema4/Imagenes/docker0.0.png?raw=true)  
Para descargar el contenedor en nuestra máquina tenemos dos opciones:
1. docker pull antonioalcm/tfg_ugr
2. sudo docker build -t buscadorbdmedical

[Enlace a DockerHub](https://hub.docker.com/r/antonioalcm/tfg_ugr/)

### Despliegue en Zeit
Para desplegar el contenedor de Docker en Zeit, debemos instalar now, para ellos usaremos npm install now -g, una vez instalado nos vamos a la carpeta donde esta el archivo Dockerfile y ejecutamos:

	sudo now --public

Con este comando nos empezará a desplegar el contenedor en Zeit

Contenedor: https://antonio-fxtswcikye.now.sh/
### Despliegue en Zeit a través de travis-cli
Para desplegar tu contenedor Docker a través de travis, lo primero que debes hacer es crear un archivo package.json, debes configurar el archivo con las siguientes líneas, estas son las líneas mínimas obligatorias:

	"scripts": {
		"clean": "now rm -y Antonio " ,
		"start": "now -e NODE_ENV=production --token $NOW_TOKEN --docker --static 		--public",
		"alias": "now alias --token $NOW_TOKEN"
	}

Una vez configurado el package.json, vamos a configurar el archivo .travis.yml, lo configuraremos para que travis lance el comando now y despliegue de forma automática el contenedor para ello configuraremos travis de la siguiente forma

	before_script: npm install now -g, npm run clean
	after_script: npm run alias
	script:
	- npm run start
	- etc...
