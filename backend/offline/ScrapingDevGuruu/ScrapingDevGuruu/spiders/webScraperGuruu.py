import scrapy
from datetime import datetime

class WebScraperSpider(scrapy.Spider):
    name = 'webscraperspider'

    custom_settings = {
                        'FEED_EXPORT_ENCODING': 'utf-8', #Establecemos la codificación de caracteres utilizada al exportar los datos de la araña, en este caso utf-8, compatible con caracteres Unicode.
                    }
    
    #Lista de urls de websites de los cuales vamos a extraer la informacion que necesitamos para nuestra base de datos (informacion relevante con respecto a Trabajo Remoto), estará en un formato final json.
    def start_requests(self):
        with open('ScrapingDevGuruu/ScrapingDevGuruu/spiders/links.txt', 'r') as f: #Abrimos el archivo links.txt en modo lectura utilizando el bloque "with" que garantiza el correcto cierre del mismo al finalizar su uso
            links = f.readlines() # Leemos todas las lineas del archivo y lo guardamos en la variable links, donde cada linea del archivo corresponde a un link o enlace.
        links = [x.strip() for x in links] # Aqui eliminamos los espacios en blanco y caracteres de nueva linea con la funcion strip().
        for link in links: #Recorremos cada link de la lista de links.
            yield scrapy.Request(url=link, callback=self.parse) #Creamos una instancia con el link como argumento de la url y self.parse como argumento del callback. Con este yield retornamos la solicitud como un generador, permitiendo a Scrapy procesarlo.


#Aqui realizamos la seleccion de cual parseador usaremos segun la url que tengamos en la lista de urls. Cada uno de estos
#parseadores son personalizados, puesto que cada pagina es diferente a la otra en al menos un aspecto.
    def parse(self, response):
        if 'extra.com.py' in response.url:
            yield from self.parse_extra(response)
        elif 'dplnews.com' in response.url:
            yield from self.parse_dplnews(response)
        elif 'abc.com.py' in response.url:
            yield from self.parse_abc(response)
        elif 'mf.com.py' in response.url:
            yield from self.parse_mf(response)
        elif 'clubdeejecutivos.org.py' in response.url:
            yield from self.parse_clubEje(response)
        elif 'marketdata.com.py' in response.url:
            yield from self.parse_marketData(response)
        elif 'foco.lanacion.com.py' in response.url:
            yield from self.parse_focoLana(response)
        elif 'usil.edu.py' in response.url:
            yield from self.parse_usil(response)
        elif 'vistage.com.py' in response.url:
            yield from self.parse_vistage(response)
        elif 'masencarnacion.com' in response.url:
            yield from self.parse_masEncar(response)
        elif 'mtess.gov.py' in response.url:
            yield from self.parse_mtess(response)
        elif 'berke.com.py' in response.url:
            yield from self.parse_berke(response)
        elif 'bacn.gov.py' in response.url:
            yield from self.parse_bacn(response)
        elif 'hoy.com.py' in response.url:
            yield from self.parse_hoy(response)
        elif 'greatplacetowork.com.py' in response.url:
            yield from self.parse_gptw(response)
        elif 'ghp.com.py' in response.url:
            yield from self.parse_ghp(response)
        elif 'taskenter.com' in response.url:
            yield from self.parse_taskEnter(response)
        elif 'blog.bayton.com.py' in response.url:
            yield from self.parse_blogBayton(response)
        elif 'infonegocios.com.py' in response.url:
            yield from self.parse_infoNegoc(response)
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#|  Seccion de parseadores personalizados por cada website                                                                                                      |
#|  Los archivos extraidos llevan la siguiente estructura:                                                                                                      | 
#|      - Titulo                                                                                                                                                |
#|      - Contenido                                                                                                                                             |
#|      - Link                                                                                                                                                  |
#|      - Fecha de scrapeo (esto para tener un control de si ya será necesario una nueva extraccion de datos pasado un X tiempo para tener info actualizada)    |
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def parse_extra(self, response):
        title = response.css('h1::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento h1 y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div.body-content p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase body-content en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link, 
            'scrape_date': date
        }
    
    def parse_dplnews(self, response):
        title = response.css('span.post-title::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento span.post-title y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div.entry-content p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase entry-content en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente #Vamos uniendo cada parte de los fragmentos de textos obtenidos anteriormente
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_abc(self, response):
        title = response.css('div.article-title h1 span::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento span dentro del elemento con clase article-title y devolvemos el valor con get() para luego asignar a variable title
        content0 = response.css('div.article-intro h2::text').get() #Obtenemos el texto de la clase compuesta por div.article-intro h2 de la estructura de la pagina web
        content = response.css('div.article-content p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase article-content en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_mf(self, response):
        title = response.css('div.blog-title h1::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento h1 dentro del elemento con clase blog-title y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div.blog-content p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase blog-content en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('meta[property="og:url"]::attr(content)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_clubEje(self, response):
        title = response.css('div.post-content h2::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase post-content y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div.post-content p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase post-content en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('div.col-md-3 a::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_marketData(self, response):
        title = response.css('h1.entry-title::text').get()#Utilizamos el selector CSS para seleccionar el contenido del elemento con clase entry-title y devolvemos el valor con get() para luego asignar a variable title
        content0 = response.css('div.entry-excerpt p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase entry-excerpt en formato de lista y lo asignamos a content0.
        content0 = ' '.join(content0) #Unimos los elementos de la lista content utilizando un espacio como separador.
        content = response.css('div.entry-content p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase entry-excerpt en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_focoLana(self, response):
        title = response.css('h1.main-title::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase main-title y devolvemos el valor con get() para luego asignar a variable title
        content0 = response.css('div.article-body i::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos i dentro del elemento con clase article-body en formato de lista y lo asignamos a content0.
        content0 = ' '.join(content0) #Unimos los elementos de la lista content utilizando un espacio como separador.
        content = response.css('div.box.type-text').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido dentro del elemento con clase box.type-text en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('div.fb-comments::attr(data-href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_usil(self, response):
        title = response.css('h2.title::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase title y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div.col-11 p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase col-11 en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_vistage(self, response):
        title = response.css('h1.press-title::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase press-title y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div.entry-content p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase entry-content en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_masEncar(self, response):
        title = response.css('div.title-post label::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase title y devolvemos el valor con get() para luego asignar a variable title
        content0 = response.css('div.title-post p::text').get() #Obtenemos el texto de la clase compuesta por div.title-post p de la estructura de la pagina web
        content = response.css('div.post p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase post en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('meta[property="og:url"]::attr(content)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_mtess(self, response):
        title = response.css('h4.page-title::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase page-title y devolvemos el valor con get() para luego asignar a variable title
        content0 = response.css('div[id="ccm-layout-column-1"] div.ccm-layout-column-inner::text').get() #Obtenemos el texto de la clase compuesta por div[id="ccm-layout-column-1"] div.ccm-layout-column-inner de la estructura de la pagina web
        content = response.css('div.ccm-layout-column-inner span').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de span dentro del elemento con clase ccm-layout-column-inner en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('form.ccm-search-block-form::attr(action)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_berke(self, response):
        title = response.css('h1.entry-title.entry--item.h2::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase h2 y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div.entry-content.entry--item p').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de p dentro del elemento con clase entry-content.entry--item en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_bacn(self, response):
        title = response.css('h1.entry-title::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase entry-title y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div.entry-content p').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de p dentro del elemento con clase entry-content en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.url #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_hoy(self, response):
        title = response.css('h1.h-b--lg.push-bottom-sm::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase push-bottom-sm y devolvemos el valor con get() para luego asignar a variable title
        content0 = response.css('header.entry-heading p::text').getall() #Utilizamos el selector CSS para seleccionar el contenido de todos los elementos p dentro del elemento con clase body-content en formato de lista y lo asignamos a content.
        content0 = ' '.join(content0) #Unimos los elementos de la lista content utilizando un espacio como separador.
        content = response.css('div.entry-text p').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de p dentro del elemento con clase entry-text en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_gptw(self, response):
        title = response.css('h1.text-left::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase text-left y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div[id="article-content"] p').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de p dentro del elemento con clase article-content en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('meta[property="og:url"]::attr(content)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_ghp(self, response):
        title = response.css('h1.h1-blog::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase h1-blog y devolvemos el valor con get() para luego asignar a variable title
        content0 = response.css('div.w-richtext blockquote::text').get() #Obtenemos el texto de la clase compuesta por div.w-richtext blockquote de la estructura de la pagina web
        content = response.css('div.w-richtext p').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de p dentro del elemento con clase w-richtext en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.url #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }

    def parse_taskEnter(self, response):
        title = response.css('h1.titleBlogShow::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase titleBlogShow y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('div.showBlogNwText p').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de p dentro del elemento con clase showBlogNwText en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_blogBayton(self, response):
        title = response.css('span[id="hs_cos_wrapper_name"]::text').get() #Utilizamos el selector CSS para seleccionar el contenido de span con id= hs_cos_wrapper_name y devolvemos el valor con get() para luego asignar a variable title
        content = response.css('span[id="hs_cos_wrapper_post_body"]').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de span con id= hs_cos_wrapper_name en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('link[rel="canonical"]::attr(href)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': content,
            'link': link,
            'scrape_date': date
        }

    def parse_infoNegoc(self, response):
        title = response.css('div.content h1::text').get() #Utilizamos el selector CSS para seleccionar el contenido del elemento con clase h1 y devolvemos el valor con get() para luego asignar a variable title
        content0 = response.css('div.description p').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de p dentro del elemento con clase description en formato de lista y lo asignamos a content.
        content0 = ' '.join(content0) #Unimos los elementos de la lista content utilizando un espacio como separador.
        content = response.css('section.body p').xpath('string()').getall() #Utilizamos el selector CSS y XPath para extraer el contenido de p dentro del elemento con clase body en formato de lista y lo asignamos a content.
        content = ' '.join(content) #Unimos los elementos de la lista content utilizando un espacio como separador.
        link = response.css('meta[property="og:url"]::attr(content)').get() #Obtenemos el link de la pagina web, en caso de que el backend indice asi lo necesite para listar al usuario la fuente de la informacion
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #La fecha del scrapeo para saber si la información ya es muy antigua y volver a scrapear en todo caso para obtener informacion actualizada
        #Emitimos un diccionario que contiene los datos extraidos de la pagina.
        yield {
            'title': title,
            'content': f'{content0} {content}',
            'link': link,
            'scrape_date': date
        }