from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to call the backend API
@app.route('/api/<endpoint>')
def call_backend(endpoint):
    http_protocol = os.environ.get("HTTP_PROTOCOL", "http")
    backend_url = os.environ.get("BACKEND_URL", "localhost:5000")
    api_url = f'{http_protocol}://{backend_url}/{endpoint}'
    response = requests.get(api_url, verify=False)
    
    if response.ok:
        return response.json()
    else:
        return {"error": "Failed to fetch data from backend"}, response.status_code

@app.route('/api/three_scale')
def three_scale():
    three_scale_url = os.environ.get("THREE_SCALE_URL", "http://localhost:5000")
    response = requests.get(three_scale_url, verify=False)
    
    if response.ok:
        return response.json()
    else:
        return {"error": response.text}, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
