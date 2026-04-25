from flask import Flask, jsonify

app = Flask(__name__)

class Item:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def to_dict(self):
        return {"name": self.name, "power": self.power}


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_strong_items(self, min_power: int) -> list:
        return [item for item in self.items if (lambda x: x.power >= min_power)(item)]


inv = Inventory()
inv.add_item(Item("Sword", 10))
inv.add_item(Item("Bow", 5))
inv.add_item(Item("Axe", 15))


@app.route("/")
def strong_items():
    items = inv.get_strong_items(10)
    return jsonify([item.to_dict() for item in items])
if __name__ == "__main__":
    app.run(debug=True, port=9001)

