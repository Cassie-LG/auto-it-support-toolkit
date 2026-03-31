from flask import Flask, render_template, jsonify
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

def load_tickets():
    tickets_file = os.path.join(BASE_DIR, "tickets.json")

    if not os.path.exists(tickets_file):
        return []
    
    with open(tickets_file) as f:
        return [json.loads(line) for line in f]
    

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/tickets")
def tickets():
    tickets = load_tickets()
    return jsonify(tickets[::-1])     #Newest first

@app.route("/latest")
def latest():
    tickets = load_tickets()
    return jsonify(tickets[-5:] if len(tickets) >= 5 else tickets)

if __name__ == "__main__":
    app.run(debug=False)