from flask import Flask, jsonify, render_template
from facts import facts
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/facts/<word>')
def get_fact(word):
    facto = facts(word)
    return jsonify(facto)



