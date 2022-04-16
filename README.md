# Overview

<b>nba-api-chatbot</b> provides a ChatBot interface to <b>NBA.com's API</b>

# Why?

I built <b>nba-api-chatbot</b> to:
* learn the basics of <b>Flask</b>
* build a <b>chatbot</b> based on <b>named entity recognition</b> using TensorFlow
* explore <b>async/await</b> in JavaScript

# Quickstart

Run with the following:
<code>python run.py</code>

This will boot up a Flask server (e.g., localhost:5000) that serves:
* a web app for interacting with the chatbot
* an API to leverage the NLP model

# Example

![example](/docs/example.png?raw=true)

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