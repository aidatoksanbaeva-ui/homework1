from flask import Flask, jsonify
app = Flask(__name__)

class Item:
    def __init__(self, id: int, name: str, power: int):
        self._id = id
        self._name = name.strip()
        self._power = power

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self._id == other._id and self._name == other._name and self._power == other._power

    def __hash__(self):
        return hash((self._id, self._name, self._power))

    def __str__(self):
        return f"Item(id={self._id}, name='{self._name}', power={self._power})"

@app.route("/")
def home():
    i = Item(1, " Sword ", 50)
    return jsonify({"item": str(i)})
if __name__ == "__main__":
    app.run(debug=True, port=6021)