import uvicorn
from fastapi import FastAPI
import random
from datetime import datetime
from collections import Counter

app = FastAPI()

class Item:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def to_dict(self):
        return {"name": self.name, "power": self.power}

class Player:
    def __init__(self, id: int, name: str, hp: int):
        self.id = id
        self.name = name
        self.hp = hp
        self.inventory = []
        self.total_damage = 0

    def take_damage(self, damage: int):
        self.hp = max(0, self.hp - damage)

    def add_item(self, item: Item):
        self.inventory.append(item)

    def attack(self, value: int):
        self.total_damage += value

class Event:
    def __init__(self, player: Player, type: str, value: int, timestamp: datetime, item: Item = None):
        self.player = player
        self.type = type
        self.value = value
        self.timestamp = timestamp
        self.item = item

    def to_dict(self):
        return {

            "player": self.player.name,
            "type": self.type,
            "value": self.value,
            "item": self.item.name if self.item else None,
            "timestamp": str(self.timestamp)
        }

def generate_events(players, items, n):
    event_types = ["ATTACK", "HEAL", "LOOT"]
    events = []
    for player in players:
        for _ in range(n):
            type_ = random.choice(event_types)
            if type_ == "ATTACK":
                value = random.randint(10, 100)
                player.attack(value)
            elif type_ == "HEAL":
                value = random.randint(5, 50)
            else:
                item = random.choice(items)
                value = item.power
                player.add_item(item)
            item_obj = item if type_ == "LOOT" else None
            events.append(Event(player, type_, value, datetime.now(), item_obj))
    return events

players = [
    Player(1, "Alice", 100),
    Player(2, "Bob", 100),
    Player(3, "Charlie", 100)
]

items = [
    Item("Sword", 25),
    Item("Bow", 15),
    Item("Axe", 40)
]

events = generate_events(players, items, 5)
log_file = "events.log"

with open(log_file, "w") as f:
    for e in events:
        f.write(str(e.to_dict()) + "\n")

def read_logs(filename):
    logs = []
    with open(filename, "r") as f:
        for line in f:
            logs.append(eval(line.strip()))
    return logs

def analyze_events(events):
    total_damage = sum(e["value"] for e in events if e["type"] == "ATTACK")
    damage_by_player = Counter()
    items_by_player = Counter()
    type_counter = Counter()
    for e in events:
        damage_by_player[e["player"]] += e["value"] if e["type"] == "ATTACK" else 0
        items_by_player[e["player"]] += 1 if e["type"] == "LOOT" else 0
        type_counter[e["type"]] += 1
    top_damage_player = max(damage_by_player, key=damage_by_player.get)
    top_items_player = max(items_by_player, key=items_by_player.get)
    most_common_event = type_counter.most_common(1)[0][0]
    return {
        "total_damage": total_damage,
        "top_damage_player": top_damage_player,
        "top_items_player": top_items_player,
        "most_common_event": most_common_event
    }

@app.get("/events")
def get_events():
    return [e.to_dict() for e in events]

@app.get("/logs")
def get_logs():
    return read_logs(log_file)

@app.get("/analytics")
def get_analytics():
    logs = read_logs(log_file)
    return analyze_events(logs)
if __name__ == "__main__":
    uvicorn.run(app, port=8200)