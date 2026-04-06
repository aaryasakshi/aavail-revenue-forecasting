from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.json
    country = data.get("country")
    date = data.get("date")

    if not country or not date:
        return jsonify({"error": "Missing input"}), 400

    result = predict(country, date)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
