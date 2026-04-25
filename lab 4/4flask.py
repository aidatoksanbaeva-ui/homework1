from flask import Flask, jsonify
app = Flask(__name__)

class Item:
    def __init__(self, item_id: int, name: str):
        self.id = item_id
        self.name = name

    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}')"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, Item) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item: Item):
        if all(i.id != item.id for i in self._items):
            self._items.append(item)

    def remove_item(self, item_id: int):
        self._items = [i for i in self._items if i.id != item_id]

    def get_items(self):
        return list(self._items)

    def unique_items(self):
        return set(self._items)

    def to_dict(self):
        return {i.id: i for i in self._items}

inv = Inventory()
inv.add_item(Item(1, "Sword"))
inv.add_item(Item(2, "Bow"))
inv.add_item(Item(3, "Shield"))

@app.route("/")
def home():
    return "Inventory API работает!"

@app.route("/items")
def items():
    return jsonify([str(i) for i in inv.get_items()])

@app.route("/unique")
def unique():
    return jsonify([str(i) for i in inv.unique_items()])

@app.route("/dict")
def dict_items():
    return jsonify({k: str(v) for k, v in inv.to_dict().items()})

@app.route("/remove/<int:item_id>")
def remove(item_id):
    inv.remove_item(item_id)
    return jsonify([str(i) for i in inv.get_items()])

if __name__ == "__main__":
    app.run(debug=True, port=5011)