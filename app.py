import json
from flask import Flask
from flask import render_template
from flask import request
from difflib import get_close_matches
data = json.load(open('data.json'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

def definition_word(word):
	if word in data:
		return data[word]

@app.route('/dictionary/', methods=['POST'])
def dictionary():
	# Input value of the given input word
	word = request.form['word']
	print(word)
	messages = definition_word(word)
	print(messages)
	if type(messages) == list:
		for message in messages:
			return render_template('home.html', word=word, message=message)
		if word.title() in data:
			word = word.title()
			messages = definition_word(word)
			for message in messages:
				return render_template('home.html', word=word, message=message)
		elif word.upper() in data:
			word = word.upper()
			messages = definition_word(word)
			for message in messages:
				return render_template('home.html', word=word, message=message)
		else:
			message = "The word doesn't exists. Please double check it."
			return render_template('home.html', word=word, message=message)
		
	else:
		if type(messages) == type(None):
			if len(get_close_matches(word, data.keys())) > 0:
				word = get_close_matches(word, data.keys())[0]
				message = f"Do you mean {word} instead?"
				return render_template('home.html', word=word, message=message)
			else:
				message = "The word doesn't exists. Please double check it."
				return render_template('home.html', word=word, message=message)
		else:
			message = "The word doesn't exists. Please double check it."
			return render_template('home.html', word=word, message=message)

if __name__ == '__main__':
	app.run(host='localhost', debug=True)