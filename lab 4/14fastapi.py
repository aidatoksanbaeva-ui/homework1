import uvicorn
from fastapi import FastAPI

app = FastAPI()

class Player:
    def __init__(self, id: int, hp: int, inventory: list):
        self.id = id
        self.hp = hp
        self.inventory = inventory

decide_action = lambda player: (
    "HEAL" if player.hp < 30
    else "LOOT" if len(player.inventory) == 0
    else "ATTACK"
)

players = [
    Player(1, 20, []),
    Player(2, 80, ["Sword"]),
    Player(3, 50, [])
]

@app.get("/decide/{player_id}")
def get_action(player_id: int):
    player = next((p for p in players if p.id == player_id), None)
    if not player:
        return {"error": "Player not found"}
    return {"player_id": player.id, "action": decide_action(player)}
if __name__ == "__main__":
    uvicorn.run(app, port=8056)