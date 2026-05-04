from flask import Flask, jsonify
from flask_cors import CORS
import db

app = Flask(__name__)
 
# Allowed port to connect to flask server

CORS(app, origins="http://127.0.0.1:3002")

# Routing grouped data

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

if __name__ == '__main__':
    app.run(debug=True, port=5001)