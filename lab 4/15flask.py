from flask import Flask, jsonify

app = Flask(__name__)

class Player:
    def __init__(self, id: int):
        self.id = id

    def process_attack(self, damage: float) -> float:
        return damage

    def process_item(self, value: float) -> float:
        return value


class Warrior(Player):
    def process_attack(self, damage: float) -> float:
        return damage * 0.9


class Mage(Player):
    def process_item(self, value: float) -> float:
        return value * 1.1


players = {
    1: Warrior(1),
    2: Mage(2)
}


@app.route("/attack/<int:player_id>/<float:damage>")
def attack(player_id, damage):
    player = players.get(player_id)
    if not player:
        return jsonify({"error": "Player not found"})
    return jsonify({
        "player_id": player.id,
        "final_damage": player.process_attack(damage)
    })


@app.route("/item/<int:player_id>/<float:value>")
def item(player_id, value):
    player = players.get(player_id)
    if not player:
        return jsonify({"error": "Player not found"})
    return jsonify({
        "player_id": player.id,
        "final_value": player.process_item(value)
    })


if __name__ == "__main__":
    app.run(debug=True, port=9003)