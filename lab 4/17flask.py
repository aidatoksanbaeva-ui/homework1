from flask import Flask, jsonify

app = Flask(__name__)

class Player:
    def __init__(self, name: str):
        self.name = name

    def __del__(self):
        print(f"Player {self.name} удалён")


players = {
    "Alice": Player("Alice"),
    "Bob": Player("Bob")
}


@app.route("/players")
def get_players():
    return jsonify(list(players.keys()))


@app.route("/delete/<name>")
def delete_player(name):
    if name in players:
        del players[name]
        return jsonify({"message": f"Player {name} deleted"})
    return jsonify({"error": "Player not found"})


if __name__ == "__main__":
    app.run(debug=True, port=8006)