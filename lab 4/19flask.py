from flask import Flask, jsonify

app = Flask(__name__)

class Item:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __repr__(self):
        return f"Item(name='{self.name}', power={self.power})"

class Inventory:
    def __init__(self, items=None):
        self.items = items or []

def analyze_inventory(inventories):
    unique_items = {item.name for inv in inventories for item in inv.items}
    all_items = [item for inv in inventories for item in inv.items]
    top_power_item = max(all_items, key=lambda x: x.power) if all_items else None
    return {
        "unique_items": list(unique_items),
        "top_power": {"name": top_power_item.name, "power": top_power_item.power} if top_power_item else None
    }

inv1 = Inventory([Item("Sword", 25), Item("Bow", 15)])
inv2 = Inventory([Item("Axe", 40), Item("Sword", 25)])

@app.route("/analyze_inventory")
def analyze():
    result = analyze_inventory([inv1, inv2])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=9017)