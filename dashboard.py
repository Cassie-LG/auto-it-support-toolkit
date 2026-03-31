from flask import Flask, render_template, jsonify
import json
from monitor import get_system_stats
from detector import detect_issues

#Load config
with open("config.json") as f:
    CONFIG = json.load(f)

    app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/status")
    def status():
        stats = get_system_stats()
        issues = detect_issues(stats, CONFIG)
        return jsonify({"stats": stats, "issues": issues})
    
    if __name__ == "__main__":
        app.run(debug=False)