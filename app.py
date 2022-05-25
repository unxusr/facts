from flask import Flask, jsonify, render_template
import facts
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/facts/<word>')
def get_fact(word):
    facto = facts.facts(word)
    return jsonify(facto)



