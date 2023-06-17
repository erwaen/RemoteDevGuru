Para utilizar el Scraper se necesita lo siguiente:
- Python 3.10
- Scrapy
- Google Translator
- Paquete ScrapeOps
-----------------------------------------------------------------------------------------------------------------------------------------------------
Ejecutar e instalar lo siguiente:
- pip install scrapy
- pip install scrapeops-scrapy-proxy-sdk
- pip install googletrans==4.0.0-rc1
-----------------------------------------------------------------------------------------------------------------------------------------------------
Luego para correr de FORMA LOCAL es el siguiente formato:

*Para el scraper de websites:*

scrapy runspider ~/webScraperGuruu.py -o ~/ubicacion_final_donde_se_quiera_guardar/websites_scraped_data.json

- La estructura de websites_scraped_data.json es el siguiente:

[{"title": "Titulo del articulo", "content": "Contenido de pagina web", "link": "link de pagina web", "scrape_date": "fecha y hora del scrapeo"}]

-----------------------------------------------------------------------------------------------------------------------------------------------------
*Para el scraper de Linkedin:*

scrapy runspider ~/Linked1N.py -o ~/ubicacion_final_donde_se_quiera_guardar/linkedin_jobs_scraped_data.json

- La estructura de linkedin_jobs_scraped_data.json es el siguiente:

[{"titulo_del_trabajo": "titulo_del_trabajo", "url_detalle_trabajo": "url_detalle_trabajo", "fue_publicado": "hace cuanto fue publicado", "nombre_empresa": "nombre_empresa", "url_empresa": "url_empresa", "ubicacion": "ubicacion del trabajo"}]

*Obs: tener en cuenta que para el scraper de Linkedin se tiene un limite de scrapeo, ya que se utiliza una API KEY de paga para saltar las medidas de seguridad que tiene
Linkedin, se tiene una cantidad gratuita pero superada la cuota ya no dejara scrapear. Dejo 2 API KEY en el codigo del spider para realizar aproximadamente 2 intentos completos de scrapeo por API KEY.
Para testeos cortos y no perder toda la cuota de una o dos veces de scrapeo, en el codigo del spider se encuentra un break comentado en el for, que al descomentar, realiza el scrapeo de 1 puesto de trabajo, pero deja scrapear como unas 8 veces el credito
de la cuenta.

-----------------------------------------------------------------------------------------------------------------------------------------------------
OBS: para correr en una sola linea se puede correr lo siguiente:

scrapy runspider ScrapingDevGuruu/ScrapingDevGuruu/spiders/webScraperGuruu.py -o websites_scraped_data.json && scrapy runspider ScrapingDevGuruu/ScrapingDevGuruu/spiders/Linked1N.py -o linkedin_jobs_data.json

-----------------------------------------------------------------------------------------------------------------------------------------------------

Para dockerizar y ejecutar los spiders desde el docker se siguen los siguientes pasos:

1-Crear un archivo con el nombre "Dockerfile" dentro del directorio principal del proyecto y que contenga lo siguiente:

FROM python:3.10

# Establecer un directorio de trabajo
WORKDIR /

# Copiar el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instalar las dependencias de la aplicación
RUN pip install -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

# Exponer el puerto que utiliza tu aplicación
EXPOSE 8000

# Ejecutar la aplicación
CMD scrapy runspider ScrapingDevGuruu/ScrapingDevGuruu/spiders/webScraperGuruu.py -o websites_scraped_data.json && scrapy runspider ScrapingDevGuruu/ScrapingDevGuruu/spiders/Linked1N.py -o linkedin_jobs_data.json

2-Crear un archivo con el nombre "requirements" y extension del tipo ".txt" dentro del directorio principal del proyecto y que contenga lo siguiente:

googletrans
numpy
python-dateutil
scrapeops-scrapy-proxy-sdk
Scrapy
scrapy
scrapy-selenium
selenium

3-Correr el siguiente comando para construir construir una imagen de Docker a partir del Dockerfile, le asignamos el nombre "backend_offline" con la etiqueta "backend_offline" y el "." especifica el directorio actual como la ubicación del Dockerfile y los archivos relacionados necesarios para construir dicha imagen:

docker build -t backend_offline:backend_offline .

4-Por ultimo correr el siguiente comando, el cual ejecutara el contenedor a partir de la imagen "backend_offline" y le asignamos el nombre "backend_offline_container":

docker run --name backend_offline_container backend_offline:backend_offline



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**TRABAJO FUTURO PARA RECOLECTAR INFO ACTUALIZADA**

**Para el caso de LinkedIn, establecí la fecha exacta del scrapeo para que pasado un tiempo X establecido deseado se pueda ir corriendo el scrapeo de nuevo y tener información actualizada. Lo unico que quedaria es configurar un proceso que lea el ultimo archivo exportado, leer la ultima fecha de scrapeo, comparar con la fecha actual y si existe tal diferencia deseada de x tiempo, volver a correr el spider scrapeador de LinkedIn.
**Para el caso de las websites, se podría implementar un spider scrapeador de google, que también necesita un metodo parecido a scrapear LinkedIn osea con una API key para el scrapeo, pero de esta manera se podria obtener los links a una cierta busqueda con palabras claves, expotar estos links en formato de lista para luego usar este archivo para pasarle a un spider que tenga una gran cantidad de formatos de web para scrapear segun la estructura de cada uno, de nuevo anotado la fecha de scrapeo para que cuando haya pasado un tiempo x establecido deseado se vuelva a correr el mismo proceso, siguiendo la misma logica del proceso del caso LinkedIn.
