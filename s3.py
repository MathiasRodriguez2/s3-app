from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

s3 = boto3.client('s3', aws_access_key_id='tu_access_key', aws_secret_access_key='tu_secret_key')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    s3.put_object(Bucket='tu_bucket_name', Key=file.filename, Body=file)
    return "File uploaded to S3"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

