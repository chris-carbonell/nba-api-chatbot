# Dependencies

# data
import requests
import urllib.parse

# flask
from flask import Flask, jsonify, render_template
from flask_cors import CORS

# NBA API ChatBot
from nba_api_chatbot.data import nba_api_constants as nac
from nba_api_chatbot import nba_api_helper as nah
from nba_api_chatbot.models import ner

# App

app = Flask("nba_api_chatbot")
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/responses/<input>", methods=['GET'])
def get_response(input):

    try:
    
        # get raw text
        text = urllib.parse.unquote(input)

        # get prediction
        prediction = ner.get_prediction(text)
        d_res = ner.extract_tagged_values(text, prediction)

        # get player details
        requested_player_name = d_res['PLAYER']
        player = nah.find_player_by_name_fuzzy(requested_player_name)
        player_name = player['full_name']
        is_active = player['is_active']

        # get stat_col
        requested_stat = d_res['STAT']
        stat_col = nac.STATS_LOOKUP[requested_stat]

        # get response
        answer = nah.get_total_stat_for_one_player(
            player_name=player_name,
            stat=stat_col
        )
        response = f"{player_name} {'has' if is_active else 'had'} {'{:,}'.format(answer)} {requested_stat}."

        return jsonify({
            'input': text,
            'output': response
            })

    except:

        return jsonify({
            'input': text,
            'output': "I don't understand. Please try again."
            })


    # Chuck Norris Example

    # try:

    #   url = "https://api.chucknorris.io/jokes/random?category=" + input
    #   # ["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music","political","religion","science","sport","travel"]

    #   r = requests.get(url)

    #   return jsonify({
    #       'input': urllib.parse.unquote(input),
    #       'output': r.json()['value']
    #       })
    
    # except:

    #   return jsonify({
    #       'input': urllib.parse.unquote(input),
    #       'output': "I don't understand."
    #       })

if __name__ == '__main__':
    app.debug = True
    app.run()