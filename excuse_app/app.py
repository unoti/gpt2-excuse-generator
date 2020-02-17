import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/excuse')
def hello_world():
    resp = {'What': 'Excuse Generator', 'output': 'something12'}
    return resp

@app.route('/excuse/gen')
def excuse():
    resp = {}
    return resp

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0')


