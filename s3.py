from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# Especificar el endpoint personalizado y las credenciales
s3 = boto3.client('s3', 
                  aws_access_key_id='6KCRlvW6KuFYYDYL9HVa', 
                  aws_secret_access_key='9Uo2AGxlRY0xuVKdeZwBZbvlA1IK9L+N+JEYIIwI',
                  endpoint_url='https://s3.openshift-storage.svc:443')  # Añadir el endpoint aquí

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    s3.put_object(Bucket='test-s3-app-bucket-eabc66c6-877d-4070-a3de-9b696377bddd',  # Solo el nombre del bucket
                  Key=file.filename, 
                  Body=file)
    return "File uploaded to S3"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

