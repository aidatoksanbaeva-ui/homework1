from flask import Flask, jsonify
from collections import Counter
from datetime import datetime

app = Flask(__name__)

class Event:
    def __init__(self, player_id: int, type: str, value: int, timestamp: datetime):
        self.player_id = player_id
        self.type = type
        self.value = value
        self.timestamp = timestamp

def analyze_logs(events):
    total_damage = sum(e.value for e in events if e.type == "ATTACK")
    damage_by_player = {}
    for e in events:
        if e.type == "ATTACK":
            damage_by_player[e.player_id] = damage_by_player.get(e.player_id, 0) + e.value

    top_player = max(damage_by_player, key=damage_by_player.get) if damage_by_player else None

    most_common_event = Counter(e.type for e in events).most_common(1)[0][0] if events else None
    return {
        "damage_by_player": damage_by_player,
        "most_common_event": most_common_event,
        "top_player": top_player
    }
events = [
    Event(1, "ATTACK", 50, datetime.now()),
    Event(2, "HEAL", 30, datetime.now()),
    Event(1, "ATTACK", 20, datetime.now()),
    Event(2, "ATTACK", 40, datetime.now()),
    Event(1, "LOOT", 10, datetime.now())
]

@app.route("/")
def analyze():
    result = analyze_logs(events)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=7078)