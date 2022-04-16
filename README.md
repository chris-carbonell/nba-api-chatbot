# Overview

<b>nba-api-chatbot</b> provides a ChatBot interface to <b>NBA.com's API</b>

# Why?

I built <b>nba-api-chatbot</b> to:
* learn the basics of <b>Flask</b>
* build a <b>chatbot</b> using <b>named entity recognition</b> built using TensorFlow
* explore <b>async/await</b> in JavaScript

# Quickstart

Run with the following:
<code>python run.py</code>

This will boot up a Flask server (e.g., localhost:5000) that serves:
* a web app for interacting with the chatbot
* an API to leverage the NLP model

# Example

![example](https://github.com/chris-carbonell/nba-api-chatbot/blob/main/docs/example.PNG)

# Named Entity Recognition

I trained a <b>named entity recognition (NER)<b> model built using TensorFlow to identify essential entities in questions like:<br>
"How many <b>points</b> did <b>Michael Jordan</b> have?"

The NER model basically tokenizes the question and tags each token with an NER label:
* tokenize:<br>
<code>["How", "many", "points", "did", "Michael", "Jordan", "have?"]</code>
* NER tag:<br>
<code>["O", "O", "B-STAT", "O", "B-PLAYER", "I-PLAYER", "O"]</code>

From there, I extract the stat ("points") and the player ("Michael Jordan"). Those inputs are scrubbed to convert the requested stat ("points") into the appropriate column name ("PTS") and, similarly, get the player's unique ID used in the API. With these two scrubbed inputs, a request is made to the API for the data and a total of that stat is summed across that player's career.

# Installation

Install the required Python dependencies:
<code>python -m pip install -r requirements.txt</code>

I'd recommend running this all in a virtual environment or a Docker container.

# Resources

* NBA API<br>
	* Python Wrapper Basics<br>
	https://github.com/swar/nba_api/blob/master/docs/examples/Basics.ipynb
* Flask
	* Basics<br>
	https://www.tutorialspoint.com/flask/flask_application.htm
	* Organizing Your Project<br>
	http://exploreflask.com/en/latest/organizing.html#package
	* Creating RESTful API<br>
	https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24
	* CORS<br>
	https://flask-cors.readthedocs.io/en/latest/
* ChatBot UI Template<br>
https://codepen.io/lilgreenland/pen/pyVvqB
* JavaScript
	* Beginner's async/await Tutorial<br>
	https://dmitripavlutin.com/javascript-fetch-async-await/
* Levenshtein Distance<br>
https://pypi.org/project/python-Levenshtein/
* NLP
	* Named Entity Recognition with TensorFlow<br>
	https://keras.io/examples/nlp/ner_transformers/

# Roadmap

* implement TensorFlow in JavaScript<br>
https://www.tensorflow.org/js