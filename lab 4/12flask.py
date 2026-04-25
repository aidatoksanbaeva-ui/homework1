from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

class Player:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Item:
    def __init__(self, id: int, name: str, power: int):
        self.id = id
        self.name = name
        self.power = power

class Event:
    def __init__(self, player_id: int, type: str, value: int, timestamp: datetime):
        self.player_id = player_id
        self.type = type
        self.value = value
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "type": self.type,
            "value": self.value,
            "timestamp": str(self.timestamp)
        }

def generate_events(players, items, n):
    events = []
    event_types = ["ATTACK", "HEAL", "LOOT"]

    for player in players:
        for _ in range(n):
            get_type = lambda: random.choice(event_types)
            event_type = get_type()

            if event_type == "ATTACK":
                value = random.randint(10, 100)
            elif event_type == "HEAL":
                value = random.randint(5, 50)
            else:
                item = random.choice(items)
                value = item.power

            event = Event(player.id, event_type, value, datetime.now())
            events.append(event)

    return events

players = [Player(1, "Alice"), Player(2, "Bob")]

items = [
    Item(1, "Sword", 25),
    Item(2, "Bow", 15)
]

@app.route("/generate_events")
def get_events():
    events = generate_events(players, items, 3)
    return jsonify([e.to_dict() for e in events])

if __name__ == "__main__":
    app.run(debug=True, port=5052)