from flask import Flask, jsonify
app = Flask(__name__)

class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")


@app.route("/")
def home():
    p = Player(1, " john ", 120)
    return jsonify({"player": str(p)})
if __name__ == "__main__":
    app.run(debug=True)