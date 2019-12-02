# Proyecto Django + Vue.js


##### Este proyecto es una prueba de concepto pero también un arquetipo listo para utilizarse, del stack Django como Backend (en este caso por defecto utiliza la versión 2.1.11 pero puede ser modificado)  Vue.js como frontend (en este caso utiliza la versión 2.6.6 pero también puede ser modificado).


##### Entre las principalesa características de este proyecto se encuentran que está listo para ser utilizado de inmediato con Docker y que a su vez se presenta en dos versiones pensadas para desarrollo y producción respectivamente. Ambas están dockerizadas pero con diferentes métodos pensadas para facilitar enormemente el desarrollo utilizando este stack. Describimos a continuación las dos variantes.


***


## Production
#### Esta versión consiste en tres imágenes de Docker, conteniendo: una la base de datos con Postgres, otra el servidor python utilizando gunicorn y otra un nginx que sirve los estáticos como reverse proxy.


***

### Estructura en la máquina host:

#### 📁 htdocs: debe contener todos los archivos con la aplicación de Django y el frontend. Si queremos usar este compose como plantilla para otro proyecto, es adentro de esta carpeta que debemos reemplazar el contenido que queremos servir. Corresponde con el contenedor que se denomina "gunicorn".


#### 📁 *nginx:* Contiene el Dockerfile y el archivo de configuración para el servidor nginx del contenedor denominado "web".


#### 📁 *postgres:* Contiene el Dockerfile y el archivo de inicialización para la base de datos de Postgres.


#### 📄 *Dockerfile:* Contiene las instrucciones para la imagen del servidor python/gunicorn que levanta el contenedor principal con el contenido de la carpeta htdocs.

#### 📄 *docker-compose:* Contiene las instrucciones para buildear y levantar los tres contenedores. Desde aquí podemos, entre otros, modificar en qué puertos va a correr cada cosa, a qué carpeta de nuestro sistema queremos que esté bindeado, el nombre, contraseña y host de nuestra base de datos




### Estructura en los contenedores

#### 📦 Contenedor *production_nginx:* Levanta el servidor nginx que funciona de proxy y sirve los estáticos. Para ello, los estáticos deben quedar en la carpeta "/site/static" dentro del contenedor. Como dichos archivos provienen a su vez del contenedor de gunicorn, el bind-mount que hagamos del contenedor de gunicorn al host con la carpeta de los estáticos (collected_assets), debe ser el mismo bind que hacemos inverso del host a este contenedor.

#### 📦 Contenedor *geropellicer/gunicorn:* Se copia toda la carpeta "htdocs" de nuestro host, a la carpeta "/site" del contenedor. Desde ahí debemos asegurarnos que los archivos estáticos que colecta propios de django, y el build de nuestro propio frontend, vayan a la carpeta "htdocs/static" para que desde ahí pasen al contendor de nginx que los sirve.

#### 📦 Contenedor *production_postgres:* Levanta el servidor de postgres con las variables de entorno que se le pasan en el docker-compose.

***


### Instrucciones

#### Prerequisitos
Python >=  3.6

Node >= 10

NPM >= 6

Docker CE >= 19

#### Clonar el repositorio
En una carpeta local que seleccionemos para trabajar, abrir una terminal y hacer git clone de este repositorio

#### Instlar dependencias de VUE y buildear el front para prod
Entramos a htdocs/frontend y buildeamos con npm:
```
cd vue-django-archetype-prod/htdocs/frontend
npm install
npm run build
```


#### Preparación de certificados SSL:
Para probar en un servidor local, este contenedor viene con un certificado SSL básico que en producción debe reemplazarse con un certificado real según el dominio que obtengamos. Dichos certificados se deben reemplazar el .crt en la carpeta "nginx/ssl/public" y el .key en la carpeta "nginx/ssl/private".

En caso de que queramos probar localmente en nuestro localhost offline:

Debemos entrar en la carpeta "nginx/ssl" y utilizamos el archivo de configuracion que se encuentra ahí para regenerar el certificado público y el privado:
````
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -config localhost.conf
````

Eso nos va a generar dos archivos (uno .key y el otro .crt). Debemos mover estos archivos a las carpetas "nginx/ssl/private" y "nginx/ssl/public" respectivamente, reemplazando el contenido que pudieran tener previamente.
````
sudo mv localhost.key ./private/
sudo mv localhost.crt ./public/
````

Preparamos nuestro sistema para que confíe en el certificado:
````
cd nginx/ssl/public
sudo apt install libnss3-tools
certutil -d sql:$HOME/.pki/nssdb -A -t "P,," -n "localhost" -i localhost.crt
````

Cerramos el navegador, rebuildeamos las imagenes con "docker-compose build" habiendo parado todos los contenedores y volver a levantar y a abrir el navegador. Todo debería estar funcionando.

## Nota:
Lo importante es que, para poder colocar los archivos de certificados SSL de encriptación (público) y decriptación (privado) deben quedar en las carpetas "nginx/ssl/public" y "nginx/ssl/private" respectivamente. Desde ahí el docker-compose.yml se encarga de colocarlos en el contenedor que tiene la imagen nginx en la ubicación correcta.

Para más info:
- https://www.humankode.com/ssl/create-a-selfsigned-certificate-for-nginx-in-5-minutes
- https://medium.com/faun/setting-up-ssl-certificates-for-nginx-in-docker-environ-e7eec5ebb418




#### Levantar usando Docker Compose
Volvemos a la raiz del proyecto:
```
cd ../.. 
```

```Docker
docker-compose up
```
El comando up intentará buscar las tres imágenes que tiene que levantar en los contenedores. Si las encuentra, es equivalente a correr "docker container run" por cada contenedor. Si no las encuentra, por ejemplo porque es la primera vez que lo ejecutamos o por que las borramos, hará primero un build de cada imagen y luego un run. 
Por lo tanto ante cada cambio que hagamos de cualquiera de los tres Dockerfiles o del mismo docker-compose.yml siempre debemos volver a hacer un docker-compose build antes de volver a levantarlo. 
Si los cambios son solo en el codigo fuente de nuestra app, ubicada en la carpeta "/htdocs", entonces no hace falta rebuildear la imagen. A lo sumo en algunos casos reiniciar los contenedores.


Ahí ya deberíamos tener las tres imágenes y la red creada. En caso de que modifiquemos algún Dockerfile o el docker-compose, debemos:
- Parar los contenedores con 
```Docker
docker-compose stop
```
- Rebuildear las imágenes con 
```Docker
docker-compose build
```
- Volver a correr los contenedores con 
```Docker
docker-compose up
```


#### Todo listo
Ya se puede visitar "localhost" y debería estar todo corriendo.

Los contenedores se puede parar y volver a levantar, o incluso para y borrar, y los cambios deberían persistir en nuestra carpeta de trabajo local.



#### Consola dentro de los contenedores
Para ejecutar una consola dentro de un contenedor (que tiene que estar corriendo), debemos obtener el id del contendor haciendo
```Docker
docker container ls
```


Una vez que tenemos en mente el ID del contendor al que queremos entrar, hacemos:
```Docker
docker container exec -it <ID del contenedor> sh 
```

*** 


### Configuraciones adicionales si venimos de la versión de local testing:

En caso de que se venga desarrollando un proyecto con la versión de local-testing de este repositorio (ver abajo) y queramos hacer un build para producción, hay algunas cosas que debemos tener en cuenta:

- En el archivo "settings.py" del proyecto de Django, debemos:
    - Setear el debug_mode a false
    - Configurar el STATIC_ROOT, STATIC_URL, MEDIA_ROOT, STATIC_DIRS como aparecen en el settings.py de este repositorio.
    - Borrar la base de datos sqlite, ya que se utilizará la de postgres.



## Nota sobre el login y register
Son las únicas dos vistas que están hechas con templates de django. Se pueden encontrar en la carpeta templates/registration y templates/django_registration. 


***

### Versión para local testing:

https://gitlab.com/devsar/innovation-lab/vue-django-archetype