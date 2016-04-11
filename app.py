from flask import Flask
import os

app = Flask(__name__)

port = int(os.getenv('PORT', '3000'))

@app.route('/')
def hello_world():
    return 'Congratulations! Welcome to the Swisscom Application Cloud.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
