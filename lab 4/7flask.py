from flask import Flask, jsonify, request
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = Flask(__name__)

class Item(BaseModel):
    id: int
    name: str
    power: int

class Event:
    def __init__(self, type: str, data: dict):
        allowed_types = {"ATTACK", "HEAL", "LOOT"}
        if type not in allowed_types:
            raise ValueError(f"Тип события должен быть одним из {allowed_types}")
        self.type = type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        ts = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"Event(type='{self.type}', data={self.data}, timestamp='{ts}')"

class Inventory:
    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item):
        if item.id not in [i.id for i in self.items]:
            self.items.append(item)

    def remove_item(self, item_id: int):
        self.items = [i for i in self.items if i.id != item_id]

    def get_items(self):
        return self.items

    def get_strong_items(self, min_power: int):
        return [item for item in self.items if item.power >= min_power]

class Player:
    def __init__(self, id: int, name: str, hp: int):
        self._id = id
        self._name = name.strip().title()
        self._hp = max(0, hp)
        self.inventory = Inventory()

    def handle_event(self, event: Event):
        if event.type == "ATTACK":
            damage = int(event.data.get("damage", 0))
            self._hp = max(0, self._hp - damage)
        elif event.type == "HEAL":
            heal = int(event.data.get("hp", 0))
            self._hp += heal
        elif event.type == "LOOT":
            item_data = event.data
            item = Item(
                id=int(item_data.get("id", 0)),
                name=str(item_data.get("name", "")),
                power=int(item_data.get("power", 0))
            )
            self.inventory.add_item(item)

    def __str__(self):
        return f"{self._name} (HP: {self._hp})"

class Warrior(Player):
    def handle_event(self, event: Event):
        if event.type == "ATTACK":
            damage = int(event.data.get("damage", 0) * 0.9)  # уменьшение урона на 10%
            self._hp = max(0, self._hp - damage)
        else:
            super().handle_event(event)

class Mage(Player):
    def handle_event(self, event: Event):
        if event.type == "LOOT":
            item_data = event.data
            power = int(item_data.get("power", 0) * 1.1)  # увеличиваем на 10%
            item = Item(
                id=int(item_data.get("id", 0)),
                name=str(item_data.get("name", "")),
                power=power
            )
            self.inventory.add_item(item)
        else:
            super().handle_event(event)

players: List[Player] = [
    Warrior(1, "Conan", 100),
    Mage(2, "Merlin", 80)
]

events: List[Event] = []

@app.route("/")
def home():
    return "Players + Inventory + Events API работает!"

@app.route("/players")
def get_players():
    return {
        p._name: {
            "hp": p._hp,
            "items": [i.dict() for i in p.inventory.get_items()]
        }
        for p in players
    }

@app.route("/create_event", methods=["POST"])
def create_event():
    data = request.get_json()
    player_id = data.get("player_id")
    type = data.get("type")
    event_data = data.get("data", {})

    try:
        event = Event(type, event_data)
    except ValueError as e:
        return {"error": str(e)}, 400

    events.append(event)

    player = next((p for p in players if p._id == player_id), None)
    if player:
        player.handle_event(event)
        return {"message": f"Event обработан для {player._name}", "event": str(event)}
    return {"error": "Игрок не найден"}, 404

@app.route("/events")
def get_events():
    return [str(e) for e in events]

@app.route("/items/<int:player_id>")
def get_items(player_id):
    player = next((p for p in players if p._id == player_id), None)
    if player:
        return [i.dict() for i in player.inventory.get_items()]
    return {"error": "Игрок не найден"}, 404

@app.route("/strong_items/<int:player_id>/<int:min_power>")
def get_strong_items(player_id, min_power):
    player = next((p for p in players if p._id == player_id), None)
    if player:
        return [i.dict() for i in player.inventory.get_strong_items(min_power)]
    return {"error": "Игрок не найден"}, 404

if __name__ == "__main__":
    app.run(debug=True, port=5005)