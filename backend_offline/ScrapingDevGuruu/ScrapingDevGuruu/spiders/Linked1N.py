import scrapy
from datetime import datetime

class LinkedtrabajosSpider(scrapy.Spider):
    name = "linkedin_trabajos"
    api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=remote%20jobs&location=Paraguay&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start=' 
    #Para poder realizar el scrapeo, utilizaremos una API KEY de prueba proporcionada por ScrapeOps y las configuraciones necesarias, ya que Linkedin es bastante agresivo previniendo cualquier tipo de scrapeo.
    #Dejare una API KEY secundaria para que el tutor pueda realizar mas tests si asi lo desea hasta que llegue al limite de la cuenta gratuita, luego de eso dejar de funcionar si no cambia de API KEY o se paga
    #la suscripcion premium. Y lo siguiente les la definicion de configuraciones personalizadas para esta araña.
    custom_settings = {'ROBOTSTXT_OBEY': False, #Indica que la araña no debe obedecer las reglas del archivo robots.txt
                       'SCRAPEOPS_API_KEY': '80355d43-84da-404d-8af0-1d37916bc802', #Clave de API para la integración con ScrapeOps, el cual es un servicio que ofrece herramientas y análisis avanzados para rastreo web.
                       #OBSERVACION: CUANDO TIRE ERROR 402 O DEJE DE FUNCIONAR EL SCRAPEO DE LINKEDIN, CAMBIAR EL KEY AL SIGUIENTE: 480a6344-7c03-4b6d-b28f-64c974d8876c
                       'SCRAPEOPS_PROXY_ENABLED': True, #Habilitamos el uso de proxies de ScrapeOps para el rastreo
                       'DOWNLOADER_MIDDLEWARES': {'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725}, #Definimos un middleware personalizado llamado ScrapeOpsScrapyProxySdk y establecemos su prioridad en 725. Este se ejecutan durante el proceso de descarga de una solicitud y permiten la manipulación de la solicitud y la respuesta.
                        'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7', #Indicamos que se utilizará una implementación específica del fingerprinter de solicitudes en Scrapy con la versión 2.7, el cual es responsable de generar identificadores únicos para las solicitudes, lo que puede ser útil para la deduplicación y el seguimiento del estado de las solicitudes.
                        'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor', #Definimos el reactor de Twisted, el cual utiliza AsyncioSelectorReactor, que es un reactor basado en Asyncio, una biblioteca de E/S asincrónica en Python.
                        'FEED_EXPORT_ENCODING': 'utf-8', #Establecemos la codificación de caracteres utilizada al exportar los datos de la araña, en este caso utf-8, compatible con caracteres Unicode.
                    }
    
    def start_requests(self):
        primer_trabajo_pagina = 0 #Definimos la variable primer_trabajo_pagina y le asignamos el valor 0, el cual representa la pagina inicial que se utilizara en la URL de solicitud. 
        first_url = self.api_url + str(primer_trabajo_pagina) #Creamos una URL inicial concatenando la variable de la api_url con el valor de primer_trabajo_pagina.
        yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'primer_trabajo_pagina': primer_trabajo_pagina}) #Devolvemos una instancia de scrapy.Request que representa la primera solicitud a realizar con yield para ser procesado por Scrapy


    def parse_job(self, response):
    
        componentes_trabajo = {} #En este diccionario guardaremos todos los campos con los datos extraidos de la pagina ya estructurado a como le necesitamos
        trabajos = response.css("li") #Aqui guardamos toda la informacion contenida en la clase li, donde esta la informacion que necesitamos scrapear

        #Segun el dato que vamos necesitando y segun la estructura de la pagina web, en este caso linkedin, vamos extrayendo los datos de los campos especificados mas abajo y los vamos guardando en
        #tanto se va recorriendo todo el codigo de la pagina web.
        for trabajo in trabajos:
            
            componentes_trabajo['titulo_del_trabajo'] = trabajo.css("h3::text").get(default='not-found').strip() #Utilizamos el selector CSS para seleccionar el elemento h3 y extraer su texto, en el caso de que este vacio devuelve "not-found" y por ultimo gracias strip() eliminamos cualquier espacio en blanco.
            componentes_trabajo['url_detalle_trabajo'] = trabajo.css(".base-card__full-link::attr(href)").get(default='not-found').strip() #Utilizamos el selector CSS para seleccionar el elemento base-card__full-link y extraer el link, en el caso de que este vacio devuelve "not-found" y por ultimo gracias strip() eliminamos cualquier espacio en blanco.
           
            componentes_trabajo['fue_publicado'] = trabajo.css('time::text').get(default='not-found').strip() #Utilizamos el selector CSS para seleccionar el elemento time y extraer su texto, en el caso de que este vacio devuelve "not-found" y por ultimo gracias strip() eliminamos cualquier espacio en blanco.
            componentes_trabajo['nombre_empresa'] = trabajo.css('h4 a::text').get(default='not-found').strip() #Utilizamos el selector CSS para seleccionar el elemento "a" y extraer su texto, en el caso de que este vacio devuelve "not-found" y por ultimo gracias strip() eliminamos cualquier espacio en blanco.
            componentes_trabajo['url_empresa'] = trabajo.css('h4 a::attr(href)').get(default='not-found') #Utilizamos el selector CSS para seleccionar el elemento "h4 a" y extraer el link, en el caso de que este vacio devuelve "not-found" y por ultimo gracias strip() eliminamos cualquier espacio en blanco.
            componentes_trabajo['ubicacion'] = trabajo.css('.job-search-card__location::text').get(default='not-found').strip() #Utilizamos el selector CSS para seleccionar el elemento ".job-search-card__location" y extraer su texto, en el caso de que este vacio devuelve "not-found" y por ultimo gracias strip() eliminamos cualquier espacio en blanco.
            
            url1 = trabajo.css(".base-card__full-link::attr(href)").get().strip() #Utilizamos el selector CSS para seleccionar el elemento base-card__full-link y extraer el link, por ultimo gracias strip() eliminamos cualquier espacio en blanco.
            yield scrapy.Request(url1, callback=self.parse_job_details, meta={'componentes_trabajo': componentes_trabajo}) #Devolvemos una instancia de scrapy.Request que representa la primera solicitud a realizar con yield para ser procesado por Scrapy, usamos el campo url1 el cual contiene la pagina con detalles del puesto de trabajo y lo pasamos al parseador "parse_job_details".
            # Además utilizamos meta: compomentes de trabajo para pasar la información ya scrapeada a través de las solicitudes y poder acceder a la misma en la funcion de devolución de llamada.
            #break # Habia dejado este break para que en los testeos no tenga que usar necesariamente toda mi cuota permitida por API KEY. Al estar comentado, posiblemente deje hacer 2 scrapeos completos como maximo.
            
            

    def parse_job_details(self, response):
        componentes_trabajo = response.meta['componentes_trabajo'] #Accedemos al diccionario componentes_trabajo que se paso como atributo meta en la solicitud anterior.
        detalle_del_puesto = response.css('div.show-more-less-html__markup.relative.overflow-hidden::text').getall() #Obtenemos el texto de la clase compuesta por div.show-more-less-html__markup.relative.overflow-hidden de la estructura de la pagina web
        detalle_del_puesto = ' '.join(detalle_del_puesto) #Unimos los elementos de la lista detalle_del_puesto utilizando un espacio como separador.
        antiguedad_requerida = response.xpath('//h3[contains(text(), "Nivel de antigüedad")]/following-sibling::span/text()').get(default='not-found').strip() #De todos los h3 que contengan el texto Seniority level, extraer el texto del inmediatamente inferior con nombre span, en el caso de que este vacio devuelve "not-found"
        tipo_empleo = response.xpath('//h3[contains(text(), "Tipo de empleo")]/following-sibling::span/text()').get(default='not-found').strip() #De todos los h3 que contengan el texto Employment type, extraer el texto del inmediatamente inferior con nombre span, en el caso de que este vacio devuelve "not-found"
        funcion_laboral = response.xpath('//h3[contains(text(), "Función laboral")]/following-sibling::span/text()').get(default='not-found').strip() #De todos los h3 que contengan el texto Job function, extraer el texto del inmediatamente inferior con nombre span, en el caso de que este vacio devuelve "not-found"
        sectores =  response.xpath('//h3[contains(text(), "Sectores")]/following-sibling::span/text()').get(default='not-found').strip() #De todos los h3 que contengan el texto Industries, extraer el texto del inmediatamente inferior con nombre span, en el caso de que este vacio devuelve "not-found"
        fecha_de_scrapeo = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Guardamos los datos en un diccionario que luego concatenaremos con lo extraido por el anterior parseador
        data = {
            'detalle_del_puesto': detalle_del_puesto,
            'antiguedad_requerida': antiguedad_requerida,
            'tipo_empleo': tipo_empleo,
            'funcion_laboral': funcion_laboral,
            'sectores': sectores,
            'fecha_de_scrapeo': fecha_de_scrapeo
        }
        componentes_trabajo.update(data) #Utilizamos el metodo update() para actualizar el diccionario componentes_trabajo, de esta manera logramos combinarlos con el resultado del anterior parseador parse_job
        yield componentes_trabajo #Finalmente con yield enviamos el diccionario componentes_trabajo como resultado de la funcion de devolucion de llamada.
        
