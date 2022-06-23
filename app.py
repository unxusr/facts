from flask import Flask, jsonify, render_template
from facts import facts
from main import brain
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/facts/<word>')
def get_fact(word):
    facto = brain(word)
    return jsonify(facto)



