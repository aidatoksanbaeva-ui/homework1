from flask import Flask, jsonify
app = Flask(__name__)

class Player:
    def __init__(self, id: int, name: str, hp: int):
        self._id = id
        self._name = name
        self._hp = hp

    @classmethod
    def from_string(cls, data: str):
        parts = data.split(",")

        if len(parts) != 3:
            raise ValueError("Неверный формат строки")

        id_str = parts[0].strip()
        name = parts[1].strip().capitalize()
        hp_str = parts[2].strip()

        if not id_str.isdigit() or not hp_str.isdigit():
            raise ValueError("id и hp должны быть числами")

        id = int(id_str)
        hp = int(hp_str)

        return cls(id, name, hp)

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

@app.route("/")
def home():
    p = Player.from_string("1, John, 100")
    return jsonify({"player": str(p)})
if __name__ == "__main__":
    app.run(debug=True, port=5001)