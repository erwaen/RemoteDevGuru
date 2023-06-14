# Establece la imagen base
FROM node:18-alpine

# Establece el directorio de trabajo en el contenedor
WORKDIR /usr/frontend

# Copia los archivos de dependencias y el archivo package-lock.json (o package.json)
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el código fuente del proyecto
COPY . .

# Expone el puerto del servidor de desarrollo de React (opcional)
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["npm", "run", "dev"]
