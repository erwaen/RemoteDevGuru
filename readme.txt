Para utilizar el Scraper se necesita lo siguiente:
- Python 3.10
- Scrapy
- Google Translator

Ejecutar e instalar lo siguiente:
- pip install scrapy
- pip install scrapeops-scrapy-proxy-sdk
- pip install googletrans==4.0.0-rc1

Luego para correr es el siguiente formato:
*Para el scraper de websites:

    - scrapy runspider ~/webScraperGuruu.py -o ~/ubicacion_final_donde_se_quiera_guardar/websites_scraped_data.json

*Para el scraper de Linkedin:

    - scrapy runspider ~/Linked1N.py -o ~/ubicacion_final_donde_se_quiera_guardar/linkedin_jobs_scraped_data.json

*Obs: tener en cuenta que para el scraper de Linkedin se tiene un limite de scrapeo, ya que se utiliza una API KEY de paga para saltar las medidas de seguridad que tiene
Linkedin, se tiene una cantidad gratuita pero superada la cuota ya no dejara scrapear.