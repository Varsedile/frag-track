from flask import Flask, jsonify
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:3002")

@app.route("/fragrances")

def fragrance():
    data = db.get_all_fragrances()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)