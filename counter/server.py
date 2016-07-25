from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "lol123"

class Counter(object):
    def __init__(self):
        self.count = 0

counter = Counter()
@app.route('/')
def index():
    counter.count += 1
    session['count'] = counter.count
    return render_template('index.html')

@app.route('/hacker')
def hacker():
    counter.count = 0
    return redirect('/')

@app.route('/ninja')
def ninja():
    counter.count += 1
    return redirect('/')


app.run(debug=True)
