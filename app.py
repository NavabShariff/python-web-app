from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def version():
    version = os.getenv('APP_VERSION', 'v1')
    return f"Current version of app is {version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)