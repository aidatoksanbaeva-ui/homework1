from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp}')"


@app.route("/")
def create_event():
    e = Event("ATTACK", {"damage": 20})
    return str(e)


if __name__ == "__main__":
    app.run(debug=True)