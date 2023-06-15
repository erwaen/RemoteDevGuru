import scrapy
from datetime import datetime
from googletrans import Translator

class WebScraperSpider(scrapy.Spider):
    name = 'webscraperspider'
    #Lista de urls de websites de los cuales vamos a extraer la informacion que necesitamos para nuestra base de datos (informacion relevante con respecto a Trabajo Remoto), estará en un formato final json.
    start_urls = ['https://www.extra.com.py/tu-dinero/rubros-trabajar-remoto-el-exterior-n2994770.html',
                  'https://dplnews.com/paraguay-ley-de-teletrabajo-la-intencion-fue-buena-pero-se-apuraron/',
                  'https://www.abc.com.py/edicion-impresa/suplementos/economico/2021/07/18/experiencias-desafios-y-perspectivas-de-la-nueva-modalidad-de-trabajo/',
                  'https://www.mf.com.py/medios/blog/experiencias-desafios-y-perspectivas-de-la-nueva-modalidad-de-trabajo.html',
                  'https://www.clubdeejecutivos.org.py/opinion/el-teletrabajo-pablo-Kalbermatten',
                  'https://marketdata.com.py/laboratorio/analisis/empleo-post-pandemia-el-futuro-incierto-del-mercado-laboral-en-paraguay-83828/',
                  'https://foco.lanacion.com.py/2023/01/16/buscas-un-trabajo-remoto-estas-app-te-seran-de-gran-ayuda/',
                  'https://www.usil.edu.py/articulo/metodologias-agiles-y-el-manejo-eficiente-de-proyectos/',
                  'http://www.vistage.com.py/ciberseguridad-los-riesgos-del-trabajo-en-remoto/',
                  'https://www.masencarnacion.com/articulo/proyecto-programando-paraguay-busca-mejorar-la-empleabilidad-de-jovenes-en-itapua-en-sector-tecnologia',
                  'https://www.mtess.gov.py/noticias/el-teletrabajo-ya-es-ley-en-paraguay-y-su-reglamentacion-esta-cargo-del-mtess-para-el-sector-privado',
                  'https://www.berke.com.py/es/ley-que-establece-la-modalidad-de-teletrabajo-en-relacion-de-dependencia/',
                  'https://www.bacn.gov.py/leyes-paraguayas/9582/ley-n-6738-establece-la-modalidad-del-teletrabajo-en-relacion-de-dependencia',
                  'https://www.hoy.com.py/tecnologia/las-10-plataformas-para-encontrar-trabajos-remotos',
                  'https://www.greatplacetowork.com.py/publicacions/blog/un-estudio-sobre-la-productividad-del-trabajo-remoto-nos-muestra-una-realidad-sorprendente-2-anos-de-analisis',
                  'https://www.ghp.com.py/blog/ley-que-regula-el-teletrabajo-en-paraguay',
                  'https://www.taskenter.com/blog/nwarticle/123/TODAS/Teletrabajo_y_Home_Office_Cuales_la_diferencia',
                  'https://blog.bayton.com.py/modelos-trabajo-hibrido-remoto-despues-pandemia',
                  'https://infonegocios.com.py/nota-principal/la-forma-sonada-de-trabajar-lo-que-hace-falta-en-paraguay-para-ser-un-nomada-digital',
                  'https://infonegocios.com.py/plus/los-trabajos-online-mas-solicitados-en-el-mundo-y-en-paraguay',
                  'https://www.linkedin.com/jobs/view/data-entry-clerk-remote-at-estaffing-inc-3549533163/?trackingId=85eihO3hnJrq%2FSsFq0KHQA%3D%3D&refId=QAg2cukTsjxq6lEcdY2phQ%3D%3D&pageNum=0&position=1&trk=public_jobs_jserp-result_search-card&originalSubdomain=py']


#Aqui realizamos la seleccion de cual parseador usaremos segun la url que tengamos en la lista de urls. Cada uno de estos
#parseadores son personalizados, puesto que cada pagina es diferente a la otra en al menos un aspecto.
    def parse(self, response):
        if 'sextra.com.py' in response.url:
            yield from self.parse_extra(response)
        elif 'sdplnews.com' in response.url:
            yield from self.parse_dplnews(response)
        elif 'sabc.com.py' in response.url:
            yield from self.parse_abc(response)
        elif 'smf.com.py' in response.url:
            yield from self.parse_mf(response)
        elif 'sclubdeejecutivos.org.py' in response.url:
            yield from self.parse_clubEje(response)
        elif 'smarketdata.com.py' in response.url:
            yield from self.parse_marketData(response)
        elif 'sfoco.lanacion.com.py' in response.url:
            yield from self.parse_focoLana(response)
        elif 'susil.edu.py' in response.url:
            yield from self.parse_usil(response)
        elif 'svistage.com.py' in response.url:
            yield from self.parse_vistage(response)
        elif 'smasencarnacion.com' in response.url:
            yield from self.parse_masEncar(response)
        elif 'smtess.gov.py' in response.url:
            yield from self.parse_mtess(response)
        elif 'sberke.com.py' in response.url:
            yield from self.parse_berke(response)
        elif 'sbacn.gov.py' in response.url:
            yield from self.parse_bacn(response)
        elif 'shoy.com.py' in response.url:
            yield from self.parse_hoy(response)
        elif 'sgreatplacetowork.com.py' in response.url:
            yield from self.parse_gptw(response)
        elif 'sghp.com.py' in response.url:
            yield from self.parse_ghp(response)
        elif 'staskenter.com' in response.url:
            yield from self.parse_taskEnter(response)
        elif 'sblog.bayton.com.py' in response.url:
            yield from self.parse_blogBayton(response)
        elif 'sinfonegocios.com.py' in response.url:
            yield from self.parse_infoNegoc(response)
        elif 'linkedin.com' in response.url:
            yield from self.parse_test(response)
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#|  Seccion de parseadores personalizados por cada website                                                                                                      |
#|  Los archivos extraidos llevan la siguiente estructura:                                                                                                      | 
#|      - Titulo                                                                                                                                                |
#|      - Contenido                                                                                                                                             |
#|      - Link                                                                                                                                                  |
#|      - Fecha de scrapeo (esto para tener un control de si ya será necesario una nueva extraccion de datos pasado un X tiempo para tener info actualizada)    |
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def parse_extra(self, response):
        title = response.css('h1::text').get() #Obtenemos el texto de la clase h1 de la estructura de la pagina web
        content = response.css('div.body-content p::text').getall() #Obtenemos el texto de la clase compuesta por div.body-content p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }
    
    def parse_dplnews(self, response):
        title = response.css('span.post-title::text').get() #Obtenemos el texto de la clase compuesta por span.post-title de la estructura de la pagina web
        content = response.css('div.entry-content p::text').getall() #Obtenemos el texto de la clase compuesta por iv.body-content p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_abc(self, response):
        title = response.css('div.article-title h1 span::text').get() #Obtenemos el texto de la clase compuesta por div.article-title h1 span de la estructura de la pagina web
        content0 = response.css('div.article-intro h2::text').get() #Obtenemos el texto de la clase compuesta por div.article-intro h2 de la estructura de la pagina web
        content = response.css('div.article-content p::text').getall() #Obtenemos el texto de la clase compuesta por span.post-title de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_mf(self, response):
        title = response.css('div.blog-title h1::text').get() #Obtenemos el texto de la clase compuesta por div.blog-title h1 de la estructura de la pagina web
        content = response.css('div.blog-content p::text').getall() #Obtenemos el texto de la clase compuesta por div.blog-content p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('meta[property="og:url"]::attr(content)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_clubEje(self, response):
        title = response.css('div.post-content h2::text').get() #Obtenemos el texto de la clase compuesta por div.post-content h2 de la estructura de la pagina web
        content = response.css('div.post-content p::text').getall() #Obtenemos el texto de la clase compuesta por div.post-content p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('div.col-md-3 a::attr(href)').get()
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_marketData(self, response):
        title = response.css('h1.entry-title::text').get() #Obtenemos el texto de la clase compuesta por h1.entry-title de la estructura de la pagina web
        content0 = response.css('div.entry-excerpt p::text').getall() #Obtenemos el texto de la clase compuesta por div.entry-excerpt p de la estructura de la pagina web
        content0 = ' '.join(content0) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        content = response.css('div.entry-content p::text').getall() #Obtenemos el texto de la clase compuesta por div.entry-content p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_focoLana(self, response):
        title = response.css('h1.main-title::text').get() #Obtenemos el texto de la clase compuesta por h1.main-title de la estructura de la pagina web
        content0 = response.css('div.article-body i::text').getall() #Obtenemos el texto de la clase compuesta por div.article-body i de la estructura de la pagina web
        content0 = ' '.join(content0) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        content = response.css('div.box.type-text').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por div.box.type-text de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('div.fb-comments::attr(data-href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_usil(self, response):
        title = response.css('h2.title::text').get() #Obtenemos el texto de la clase compuesta por h2.title de la estructura de la pagina web
        content = response.css('div.col-11 p::text').getall() #Obtenemos el texto de la clase compuesta por div.col-11 p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_vistage(self, response):
        title = response.css('h1.press-title::text').get() #Obtenemos el texto de la clase compuesta por h1.press-title de la estructura de la pagina web
        content = response.css('div.entry-content p::text').getall() #Obtenemos el texto de la clase compuesta por div.entry-content p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_masEncar(self, response):
        title = response.css('div.title-post label::text').get() #Obtenemos el texto de la clase compuesta por div.title-post label de la estructura de la pagina web
        content0 = response.css('div.title-post p::text').get() #Obtenemos el texto de la clase compuesta por div.title-post p de la estructura de la pagina web
        content = response.css('div.post p::text').getall() #Obtenemos el texto de la clase compuesta por div.post p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('meta[property="og:url"]::attr(content)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_mtess(self, response):
        title = response.css('h4.page-title::text').get() #Obtenemos el texto de la clase compuesta por h4.page-title de la estructura de la pagina web
        content0 = response.css('div[id="ccm-layout-column-1"] div.ccm-layout-column-inner::text').get() #Obtenemos el texto de la clase compuesta por div[id="ccm-layout-column-1"] div.ccm-layout-column-inner de la estructura de la pagina web
        content = response.css('div.ccm-layout-column-inner span').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por div.ccm-layout-column-inner span de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('form.ccm-search-block-form::attr(action)').get()
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_berke(self, response):
        title = response.css('h1.entry-title.entry--item.h2::text').get() #Obtenemos el texto de la clase compuesta por h1.entry-title.entry--item.h2 de la estructura de la pagina web
        content = response.css('div.entry-content.entry--item p').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por div.entry-content.entry--item p label de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_bacn(self, response):
        title = response.css('h1.entry-title::text').get() #Obtenemos el texto de la clase compuesta por h1.entry-title de la estructura de la pagina web
        content = response.css('div.entry-content p').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por div.entry-content p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.url
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_hoy(self, response):
        title = response.css('h1.h-b--lg.push-bottom-sm::text').get() #Obtenemos el texto de la clase compuesta por h1.h-b--lg.push-bottom-sm de la estructura de la pagina web
        content0 = response.css('header.entry-heading p::text').getall() #Obtenemos el texto de la clase compuesta por header.entry-heading p de la estructura de la pagina web
        content0 = ' '.join(content0) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        content = response.css('div.entry-text p').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por div.entry-text p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_gptw(self, response):
        title = response.css('h1.text-left::text').get() #Obtenemos el texto de la clase compuesta por h1.text-left de la estructura de la pagina web
        content = response.css('div[id="article-content"] p').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por div[id="article-content"] p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('meta[property="og:url"]::attr(content)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_ghp(self, response):
        title = response.css('h1.h1-blog::text').get() #Obtenemos el texto de la clase compuesta por h1.h1-blog de la estructura de la pagina web
        content0 = response.css('div.w-richtext blockquote::text').get() #Obtenemos el texto de la clase compuesta por div.w-richtext blockquote de la estructura de la pagina web
        content = response.css('div.w-richtext p').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por div.w-richtext p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.url
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_taskEnter(self, response):
        title = response.css('h1.titleBlogShow::text').get() #Obtenemos el texto de la clase compuesta por h1.titleBlogShow de la estructura de la pagina web
        content = response.css('div.showBlogNwText p').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por div.showBlogNwText p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_blogBayton(self, response):
        title = response.css('span[id="hs_cos_wrapper_name"]::text').get() #Obtenemos el texto de la clase compuesta por span[id="hs_cos_wrapper_name"] de la estructura de la pagina web
        content = response.css('span[id="hs_cos_wrapper_post_body"]').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por span[id="hs_cos_wrapper_post_body"] de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_infoNegoc(self, response):
        title = response.css('div.content h1::text').get() #Obtenemos el texto de la clase compuesta por div.content h1 de la estructura de la pagina web
        content0 = response.css('div.description p').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por div.description p de la estructura de la pagina web
        content0 = ' '.join(content0) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente 
        content = response.css('section.body p').xpath('string()').getall() #Obtenemos el texto de la clase compuesta por section.body p de la estructura de la pagina web
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('meta[property="og:url"]::attr(content)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_test(self, response):
        title = response.css('div.show-more-less-html__markup.relative.overflow-hidden::text').getall() #Obtenemos el texto de la clase compuesta por div.show-more-less-html__markup.relative.overflow-hidden de la estructura de la pagina web
        title = ' '.join(title) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        antiguedad = response.xpath('//h3[contains(text(), "Seniority level")]/following-sibling::span/text()').get() #De todos los h3 que contengan el texto Seniority level, extraer el texto del inmediatamente inferior con nombre span
        tipo_empleo = response.xpath('//h3[contains(text(), "Employment type")]/following-sibling::span/text()').get() #De todos los h3 que contengan el texto Employment type, extraer el texto del inmediatamente inferior con nombre span
        funcion_laboral = response.xpath('//h3[contains(text(), "Job function")]/following-sibling::span/text()').get() #De todos los h3 que contengan el texto Job function, extraer el texto del inmediatamente inferior con nombre span
        sectores =  response.xpath('//h3[contains(text(), "Industries")]/following-sibling::span/text()').get() #De todos los h3 que contengan el texto Industries, extraer el texto del inmediatamente inferior con nombre span
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Escribimos los datos obtenidos y los estructuramos todos por igual
        yield {
            'title': title,
            'antiguedad': antiguedad,
            'tipo_empleo': tipo_empleo,
            'funcion_laboral': funcion_laboral,
            'sectores': sectores,
            'scrape_date': date
        }