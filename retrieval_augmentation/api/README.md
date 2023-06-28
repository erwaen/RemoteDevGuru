# **Retrieval augmentation API**

This API performs a similarity searches and retrieval augmented
generative question answering on information stored in a Pinecone
database.

## **Similarity searches**

### **Request**

`POST /similarity search`

```
{
  "query_content": "data entry clerk"
}
```

### **Response**

```
{
  "results": [
    {
      "page_content": "Job Tittle- Data Entry Clerk - Remote Job location- Remote Salary Depending on Candidate Experience Opening Required 10 Data entry operator. Fresher can also apply. Enter data into system accurately and efficiently Organize and maintain files and records Perform other duties as assigned by the supervisor. Compiling, verifying the accuracy, and sorting information to prepare source data for computer entry. Reviewing data for deficiencies or errors, correcting any incompatibilities, and checking output. Required Candidate profile. GOOD KNOWLEDGE OF COMPUTER MUST HAVE LAPTOP OR SYSTEM MUST HAVE BASIC TYPING SPEED MUST HAVE TYPING ACCURACY NO WORK PRESSURE & NO TIME BOUNDATION",
      "metadata": {
        "date_of_scrapping": "2023-06-17T23:10:43",
        "job_title": "Data Entry Clerk - Remote",
        "seq_num": 1,
        "source": "https://py.linkedin.com/jobs/view/data-entry-clerk-remote-at-estaffing-inc-3549533163?refId=Rl4dJdGCnUXHvz5znJDy%2Fg%3D%3D&trackingId=GiDE%2BABmZCzZnciUJJOuqA%3D%3D&position=1&pageNum=0&trk=public_jobs_jserp-result_search-card"
      }
    }
  ]
}
```

## **Retrieval augmented generative question answering**

### **Request**

`POST /qa`

```
{
  "query_content": "What are the dangers of cyberattacks?"
}
```

### **Response**

```
{
  "results": [
    {
      "page_content": "Los ciberataques son una amenaza de peso en las economías ya en circunstancias normales. Pueden hacer que tu negocio se detenga por completo en un santiamén. Y en el mundo del COVID-19, la seguridad cibernética se ha vuelto aún más crítica ya que, de repente, los trabajadores remotos se exponen, sin quererlo, a los ciberdelincuentes. Nuestros datos muestran que solo el 46% de las pequeñas y medianas empresas (PYMES) tienen una estrategia de ciberseguridad activa y actualizada. Sin embargo, incluso las tecnologías y estrategias cibernéticas más avanzadas no pueden proteger a la empresa contra el eslabón más débil: sus empleados en remoto. Las personas siempre han sido el eslabón más débil de una estrategia de seguridad cibernética en capas de personas, procesos y tecnología en tiempos normales. Con los trabajadores que funcionan de forma remota desde las oficinas en sus casas, la amenaza y la exposición son aún mayores. Los trabajadores remotos están trabajando en sus redes personales, fuera de las VPN y más allá de los firewalls, lo que aumenta su riesgo y abre la puerta a ciberdelincuentes cada vez más astutos. Además de los problemas y desafíos comerciales de funcionar en el mundo COVID, ¿cuál sería el impacto para tu negocio de tener todos sus datos como rehenes? ¿Cómo afectaría un ataque masivo de ransomware y el pago de los ciberdelincuentes a tu flujo de caja, especialmente si eres una del 33% de las pymes que tienen cinco meses o menos de efectivo disponible? La buena noticia de",
      "metadata": {
        "article_title": "Ciberseguridad: los riesgos del trabajo en remoto",
        "date_of_scrapping": "2023-06-13T12:46:14",
        "seq_num": 2,
        "source": "http://www.vistage.com.py/ciberseguridad-los-riesgos-del-trabajo-en-remoto/"
      }
    }
  ]
}
```
