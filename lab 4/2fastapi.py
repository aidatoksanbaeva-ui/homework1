from fastapi import FastAPI
import uvicorn
app = FastAPI()

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

@app.get("/")
def read_root():
    p = Player.from_string("2, alice, 90")
    return {"player": str(p)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)