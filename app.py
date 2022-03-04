"""Main script, uses other modules to generate sentences."""
from glob import glob
from flask import Flask, render_template, flash, redirect, request
from make_tokens import get_tokens
from markav_chain import Markov, Markov2
import twitter

app = Flask(__name__)

mark = None

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    global mark
    tokens = get_tokens('data/script.txt')
    mark = Markov2(tokens)

@app.route('/tweet', methods=['POST'])
def tweet():
    sentence = request.form['sentence']
    print(sentence)
    status = twitter.tweet(sentence)
    print(status)
    return redirect('/')

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    global mark
    return render_template('index.html', sentence=mark.walk())


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
