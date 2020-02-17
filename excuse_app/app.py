print('App Loading')
import os
from flask import Flask, request

from excuses import ExcuseSituation
from textgen import TextGenerator

app = Flask(__name__)

#model_size = 'gpt2-xl'  # Too much for CPU-based inference.
model_size = 'gpt2'
gen = TextGenerator(model_size)

@app.route('/excuse')
def hello_world():
    resp = {'What': 'Excuse Generator', 'output': 'something13'}
    return resp

@app.route('/excuse/gen')
def excuse():
    s = ExcuseSituation(gen, assignment="prepare a nice dinner for you for Valentine's day", tasks=[
        'plan the menu',
        'go to the grocery store to buy the ingredients',
        'cook it up',
        'plate the meal in an attractive way',
    ])
    excuses = s.generate_excuses(count=3)
    result =  {
        'excuses' : excuses
    }
    return result

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print('App Ready')
    app.run(debug=True, host='0.0.0.0')


