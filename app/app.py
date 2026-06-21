from flask import Flask, jsonify

app = Flask(__name__)

expenses = [
    {"id": 1, "title": "Food", "amount": 500},
    {"id": 2, "title": "Travel", "amount": 1200}
]

@app.route("/")
def home():
    return jsonify({
        "message": "Expense Tracker API Running 🚀"
    })

@app.route("/expenses")
def get_expenses():
    return jsonify(expenses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)