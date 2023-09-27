
# Utiliza una imagen base de Python
FROM python

# Establece un directorio de trabajo
WORKDIR /app

# Instala las dependencias necesarias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu script y templates
COPY s3.py .
COPY templates/ ./templates/

# Comando para ejecutar tu script
CMD ["python", "./s3.py"]

