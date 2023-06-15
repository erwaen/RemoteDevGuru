import scrapy
from datetime import datetime

class LinkedtrabajosSpider(scrapy.Spider):
    name = "linkedin_trabajos"
    api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=remote%20jobs&location=Paraguay&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start=' 
    #Para poder realizar el scrapeo, utilizaremos una API KEY de prueba proporcionada por ScrapeOps y las configuraciones necesarias, ya que Linkedin es bastante agresivo previniendo cualquier tipo de scrapeo.
    #Dejare una API KEY secundaria para que el tutor pueda realizar mas test si asi lo desea hasta que llegue al limite de la cuenta gratuita, luego de eso dejar de funcionar si no cambia de API KEY o se paga
    #la suscripcion premium.
    custom_settings = {'ROBOTSTXT_OBEY': False, 'SCRAPEOPS_API_KEY': 'ce640ebc-6878-479d-8586-b58e291b9cc7',
                       'SCRAPEOPS_PROXY_ENABLED': True, 
                       'DOWNLOADER_MIDDLEWARES': {'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725},
                        'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
                        'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',
                        'FEED_EXPORT_ENCODING': 'utf-8',
                        }
    #Iniciamos la peticion llamando con un callback de la primera url a la funcion de scrapeo
    def start_requests(self):
        primer_trabajo_pagina = 0
        first_url = self.api_url + str(primer_trabajo_pagina)
        yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'primer_trabajo_pagina': primer_trabajo_pagina})


    def parse_job(self, response):
    
        componentes_trabajo = {} #aqui guardaremos todos los campos con los datos extraidos de la pagina ya estructurado a como le necesitamos
        trabajos = response.css("li") #aqui indicamos cual subclase estareamos targeteando para encontrar los datos que solicitaremos mas abajo y lo guardamos en variable trabajos
        componentes_detalles = {}

        
        num_trabajos_encontrados = len(trabajos) #contador de cantidad de trabajos encontrados en la primera pagina de linkedin (mas paginas van apareciendo a medida que bajamos el scroll)
        print("******* Numero de Trabajos *******")
        print(num_trabajos_encontrados) #imprimimos la cantidad de trabajos
        print('*****')
        #Segun el dato que vamos necesitando y segun la estructura de la pagina web, en este caso linkedin, vamos extrayendo los datos de los campos especificados mas abajo y los vamos guardando en
        #tanto se va recorriendo todo el codigo de la pagina web.
        for trabajo in trabajos:
            
            componentes_trabajo['titulo_del_trabajo'] = trabajo.css("h3::text").get(default='not-found').strip()
            componentes_trabajo['url_detalle_trabajo'] = trabajo.css(".base-card__full-link::attr(href)").get(default='not-found').strip()
            url_trabajo_actual = trabajo.css(".base-card__full-link::attr(href)").get(default='not-found').strip()
            detalles = response.follow(url_trabajo_actual, callback=self.parse_job_details) #Llamamos al scrapeador de la subpagina donde estan los detalles del trabajo remoto
            for detalle in detalles:
                componentes_detalles['detalle_del_puesto'] = detalle.css('detalle_del_puesto::text').get(default='not-found').strip()
                yield componentes_detalles

            componentes_trabajo['fue_publicado'] = trabajo.css('time::text').get(default='not-found').strip()
            componentes_trabajo['nombre_empresa'] = trabajo.css('h4 a::text').get(default='not-found').strip()
            componentes_trabajo['url_empresa'] = trabajo.css('h4 a::attr(href)').get(default='not-found')
            componentes_trabajo['ubicacion'] = trabajo.css('.job-search-card__location::text').get(default='not-found').strip()
            componentes_trabajo['fecha_de_scrapeo'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
            yield componentes_trabajo

    def parse_job_details(self, response):
        detalle_del_puesto = response.css('div.show-more-less-html__markup.relative.overflow-hidden::text').getall() #Obtenemos el texto de la clase compuesta por div.show-more-less-html__markup.relative.overflow-hidden de la estructura de la pagina web
        detalle_del_puesto = ' '.join(detalle_del_puesto) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        antiguedad = response.xpath('//h3[contains(text(), "Seniority level")]/following-sibling::span/text()').get() #De todos los h3 que contengan el texto Seniority level, extraer el texto del inmediatamente inferior con nombre span
        tipo_empleo = response.xpath('//h3[contains(text(), "Employment type")]/following-sibling::span/text()').get() #De todos los h3 que contengan el texto Employment type, extraer el texto del inmediatamente inferior con nombre span
        funcion_laboral = response.xpath('//h3[contains(text(), "Job function")]/following-sibling::span/text()').get() #De todos los h3 que contengan el texto Job function, extraer el texto del inmediatamente inferior con nombre span
        sectores =  response.xpath('//h3[contains(text(), "Industries")]/following-sibling::span/text()').get() #De todos los h3 que contengan el texto Industries, extraer el texto del inmediatamente inferior con nombre span
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'detalle_del_puesto': detalle_del_puesto,
            'antiguedad': antiguedad,
            'tipo_empleo': tipo_empleo,
            'funcion_laboral': funcion_laboral,
            'sectores': sectores
        }


        
