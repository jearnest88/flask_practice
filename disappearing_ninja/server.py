from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja/')
def ninja():
	return render_template('ninja.html', ninja='all')

@app.route('/ninja/<ninja_color>/')
def ninja_color(ninja_color):
	return render_template('ninja.html', ninja=ninja_color)

app.run(debug=True)
