from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import db
from dotenv import load_dotenv
import os
import scrape

load_dotenv()

app = Flask(__name__)
 
# Allowed port to connect to flask server

CORS(app, origins="https://frag-track-app.onrender.com")

# Routing grouped data

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fragrance")
def fragrance_page():
    return render_template("fragrance.html")

@app.route("/fragrances")
def fragrance():
    data = db.get_all_fragrances()
    return jsonify(data)

# Routing seperate data by ID

@app.route("/fragrances/<int:id>")
def show_id(id):
    data = db.get_one_fragrance(id)
    return jsonify(data)

# Routing price history by ID

@app.route("/fragrances/<int:id>/history")
def show_price_history(id):
    data = db.get_price_history(id)
    return jsonify(data)

@app.route("/run-scraper")
def run_scraper():
    token = request.args.get("token")
    if token == os.getenv("secret_token"):
        scrape.run_scraping()
        return "OK", 200
    else: 
        return "Unauthorized", 403

if __name__ == '__main__':
    app.run(debug=True, port=5001)