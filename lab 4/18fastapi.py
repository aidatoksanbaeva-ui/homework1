from flask import Flask, jsonify

app = Flask(__name__)

class Item:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def to_dict(self):
        return {"name": self.name, "power": self.power}

class Inventory:
    def __init__(self, items=None):
        self.items = items or []

    def add_item(self, item: Item):
        self.items.append(item)

    def __iter__(self):
        return iter(self.items)

    def powerful_items(self, threshold: int):
        return [item for item in self.items if item.power >= threshold]


inventory = Inventory([
    Item("Sword", 25),
    Item("Bow", 15),
    Item("Axe", 40)
])

@app.route("/items")
def get_items():
    return jsonify([item.to_dict() for item in inventory])

@app.route("/powerful/<int:threshold>")
def get_powerful(threshold):
    return jsonify([item.to_dict() for item in inventory.powerful_items(threshold)])

if __name__ == "__main__":
    app.run(debug=True, port=6066)