# Para utilizar el Scraper se necesita lo siguiente: 
- Python 3.10
- Scrapy
- Google Translator
- Paquete ScrapeOps

# Ejecutar e instalar lo siguiente:
- pip install scrapy
- pip install scrapeops-scrapy-proxy-sdk
- pip install googletrans==4.0.0-rc1

# Luego para correr de **forma local** es el siguiente formato:
## Para el scraper de websites:

```
scrapy runspider /directorio_donde_se_encuentre_proyecto/ScrapingDevGuruu/ScrapingDevGuruu/spiders/webScraperGuruu.py -o /ubicacion_final_donde_se_quiera_guardar/websites_scraped_data.json
 ```

### La estructura de websites_scraped_data.json es el siguiente:
```
[{"title": "Titulo del articulo", "content": "Contenido de pagina web", "link": "link de pagina web", "scrape_date": "fecha y hora del scrapeo"}]
```

## Para el scraper de Linkedin:
```
scrapy runspider /directorio_donde_se_encuentre_proyecto/ScrapingDevGuruu/ScrapingDevGuruu/spiders/Linked1N.py -o /ubicacion_final_donde_se_quiera_guardar/linkedin_jobs_scraped_data.json
```
### La estructura de linkedin_jobs_scraped_data.json es el siguiente:
```
[{"titulo_del_trabajo": "titulo_del_trabajo", "url_detalle_trabajo": "url_detalle_trabajo", "fue_publicado": "hace cuanto fue publicado", "nombre_empresa": "nombre_empresa", "url_empresa": "url_empresa", "ubicacion": "ubicacion del trabajo"}, {"detalle_del_puesto": "detalle_del_puesto", "antiguedad_requerida": "antiguedad_requerida", "tipo_empleo": "tipo_empleo", "funcion_laboral": "funcion_laboral", "sectores": "sectores", "fecha_de_scrapeo": "fecha_de_scrapeo"}]
```
>**Obs:** tener en cuenta que para el scraper de Linkedin se tiene un límite de scrapeo, ya que se utiliza una API KEY de paga para saltar las medidas de seguridad que tiene Linkedin, se tiene una cantidad gratuita pero superada la cuota ya no dejara scrapear. Dejo 2 API KEY en el código del spider para realizar aproximadamente 2 intentos completos de scrapeo por API KEY. Para testeos cortos y no perder toda la cuota de una o dos veces de scrapeo, en el código del spider se encuentra un break comentado en el for, que al descomentar, realiza el scrapeo de 1 puesto de trabajo, pero deja scrapear como unas 8 veces el crédito de la cuenta.

## OBS: para correr en una sola linea se puede correr lo siguiente:
```
scrapy runspider ScrapingDevGuruu/ScrapingDevGuruu/spiders/webScraperGuruu.py -o websites_scraped_data.json && scrapy runspider ScrapingDevGuruu/ScrapingDevGuruu/spiders/Linked1N.py -o linkedin_jobs_data.json
 ```

# Para dockerizar y ejecutar los spiders desde el docker se siguen los siguientes pasos:

 1. Correr el siguiente comando para construir construir una imagen de Docker a partir del Dockerfile, le asignamos el nombre "backend_offline" con la etiqueta "backend_offline" y el "." especifica el directorio actual como la ubicación del Dockerfile y los archivos relacionados necesarios para construir dicha imagen:
``` 
docker build -t backend_offline:backend_offline .
```
 2. Por ultimo correr el siguiente comando, el cual ejecutara el contenedor a partir de la imagen "backend_offline" y le asignamos el nombre "backend_offline_container":
 ```
 docker run --name backend_offline_container backend_offline:backend_offline.
 ```

# Con docker-compose se mapeo a un volumen local para que los resultados se queden en nuestra maquina y no en el contenedor

1. Buildear
```
docker-compose build
```
2. Levantar (correr)
```
docker-compose up
```

# Trabajo furuto para recolectar información actualizada

>**Para el caso de LinkedIn**: establecí la fecha exacta del scrapeo para que pasado un tiempo X establecido deseado se pueda ir corriendo el scrapeo de nuevo y tener información actualizada. Lo unico que quedaria es configurar un proceso que lea el ultimo archivo exportado, leer la ultima fecha de scrapeo, comparar con la fecha actual y si existe tal diferencia deseada de x tiempo, volver a correr el spider scrapeador de LinkedIn.

>**Para el caso de las websites**: se podría implementar un spider scrapeador de google, que también necesita un metodo parecido a scrapear LinkedIn osea con una API key para el scrapeo, pero de esta manera se podria obtener los links a una cierta busqueda con palabras claves, expotar estos links en formato de lista para luego usar este archivo para pasarle a un spider que tenga una gran cantidad de formatos de web para scrapear segun la estructura de cada uno, de nuevo anotado la fecha de scrapeo para que cuando haya pasado un tiempo x establecido deseado se vuelva a correr el mismo proceso, siguiendo la misma logica del proceso del caso LinkedIn.