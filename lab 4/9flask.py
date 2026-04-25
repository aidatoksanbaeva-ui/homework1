from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

class Event:
    def __init__(self, type: str, data: dict, timestamp: datetime):
        self.type = type
        self.data = data
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "type": self.type,
            "data": self.data,
            "timestamp": str(self.timestamp)
        }

class Logger:
    def read_logs(self, filename: str) -> list:
        events = []

        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                timestamp, player_id, event_type, data = line.split(";", 3)

                event = Event(
                    event_type,
                    eval(data),
                    datetime.fromisoformat(timestamp)
                )

                events.append(event)

        return events


logger = Logger()

@app.route("/logs")
def get_logs():
    events = logger.read_logs("logs.txt")
    return jsonify([e.to_dict() for e in events])

if __name__ == "__main__":
    app.run(debug=True, port=9002)