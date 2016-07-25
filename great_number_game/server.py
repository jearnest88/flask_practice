from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "123lol"

class generateNum(object):
    def __init__(self):
        self.number = 0
    def generate(self):
        self.number = random.randrange(0,101)

gen = generateNum()
gen.generate()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def get_number():
    session['random'] = gen.number
    session['guess'] = int(request.form['num_guess'])
    print session['random']
    if session['guess'] > session['random']:
        session['attempt'] = 1 #guess is too high
    elif session['guess'] < session['random']:
        session['attempt'] = 2  #guess it too low
    else:
        session['attempt'] = 3   #guess is correct

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['attempt'] = 4
    gen.generate()
    return redirect('/')

app.run(debug=True)
