from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = 'lol123'

class Work(object):
    def __init__(self):
        self.count = 0

gold = Work()

@app.route('/')
def index():
    session['gold_count'] = gold.count
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    labor = request.form['labor']
    if labor == 'farm':
        gold.count += 10
        flash("Working hard on the farm earned you 10 gold!", 'gold')
    elif labor == 'cave':
        gold.count += 5
        flash("Stumbling in the cave you found 5 gold!", 'gold')
    elif labor == 'house':
        gold.count += 3
        flash("Found some change in the cushions, 3 gold!", 'gold')
    elif labor == 'casino':
        gold.count += 40
        flash("Bet everything and won 40 gold!", 'gold')
    return redirect('/')

@app.route('/reset')
def reset():
    print "Gold is gone!"
    session.pop('gold_count')
    gold.count = 0
    return redirect('/')

app.run(debug=True)
