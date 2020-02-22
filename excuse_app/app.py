print('App Loading')
import os
from flask import Flask, request
from flask_socketio import SocketIO

from excuses import ExcuseSituation
from textgen import TextGenerator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so secret'
socketio = SocketIO(app, cors_allowed_origins=['http://localhost:3000'])

#model_size = 'gpt2-xl'  # Too much for CPU-based inference.

#model_size = 'gpt2'
#gen = TextGenerator(model_size)

@app.route('/excuse')
def hello_world():
    resp = {'What': 'Excuse Generator', 'output': 'something13'}
    return resp

"""
@app.route('/excuse/gen')
def excuse():
    def show_word(w):
        print('>', w)

    s = ExcuseSituation(gen, assignment="prepare a nice dinner for you for Valentine's day", tasks=[
        'plan the menu',
        'go to the grocery store to buy the ingredients',
        'cook it up',
        'plate the meal in an attractive way',
    ], word_callback=show_word)
    excuses = s.generate_excuses(count=3)
    result =  {
        'excuses' : excuses
    }
    return result
"""

@socketio.on('my event')
def handle_message(data):
    print('< ' + str(data))

if __name__ == '__main__':
    print('App Ready')
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)


