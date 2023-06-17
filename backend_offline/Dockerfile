# Usamos la imagen base de python
FROM python:3.10

# Establecemos un directorio de trabajo
WORKDIR /

# Copiamos el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instalamos las dependencias de la aplicación
RUN pip install -r requirements.txt

# Copiamos el resto del código de la aplicación al contenedor
COPY . .

# Exponemos el puerto que utiliza tu aplicación
EXPOSE 8000

# Ejecutamos la aplicación
CMD scrapy runspider ScrapingDevGuruu/ScrapingDevGuruu/spiders/webScraperGuruu.py -o websites_scraped_data.json && scrapy runspider ScrapingDevGuruu/ScrapingDevGuruu/spiders/Linked1N.py -o linkedin_jobs_data.json
