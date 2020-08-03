import json
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

def definition_word(word):
	data = json.load(open('data.json'))
	if word in data:
		return data[word]

@app.route('/dictionary/', methods=['POST'])
def dictionary():
	# Input value of the given input word
	word = request.form['word']
	print(word)
	message = definition_word(word)
	print(message)
	if type(message) == list:
		return render_template('home.html', word=word, message=message)
	elif type(message) == type(None):
		message = "The word doesn't exists. Please double check it."
		return render_template('home.html', message=message)
	else:
		message = "Sorry, we didn't understand. Please try again!"
		return render_template('home.html', message=message)

if __name__ == '__main__':
	app.run(host='localhost', debug=True)