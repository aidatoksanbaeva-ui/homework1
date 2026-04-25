import uvicorn
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

class Event:
    def __init__(self, type: str, data: dict):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()

class Player:
    def __init__(self, player_id: int):
        self.player_id = player_id

class Logger:
    def log(self, event: Event, player: Player, filename: str):
        line = f"{event.timestamp};{player.player_id};{event.type};{event.data}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)


logger = Logger()

@app.get("/log")
def write_log():
    player = Player(1)
    event = Event("ATTACK", {"damage": 20})

    logger.log(event, player, "logs.txt")

    return {
        "message": "Logged successfully",
        "event": {
            "type": event.type,
            "data": event.data,
            "timestamp": str(event.timestamp)
        },
        "player_id": player.player_id
    }
if __name__ == "__main__":
    uvicorn.run(app, port=8065)