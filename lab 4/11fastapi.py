import uvicorn
from fastapi import FastAPI
from datetime import datetime
from typing import List, Iterator

class Event:
    def __init__(self, id: int, type: str, value: int, timestamp: datetime):
        self.id = id
        self.type = type
        self.value = value
        self.timestamp = timestamp

    def __repr__(self):
        return f"Event(id={self.id}, type='{self.type}', value={self.value}, timestamp='{self.timestamp}')"

def damage_stream(events: List[Event]) -> Iterator[int]:
    for event in events:
        if event.type == "ATTACK":
            yield event.value

app = FastAPI()

events = [
    Event(1, "ATTACK", 50, datetime.now()),
    Event(2, "HEAL", 30, datetime.now()),
    Event(3, "ATTACK", 20, datetime.now()),
    Event(4, "HEAL", 10, datetime.now()),
    Event(5, "ATTACK", 35, datetime.now())
]

damage_generator = damage_stream(events)

@app.get("/next_damage")
def get_next_damage():
    try:
        damage = next(damage_generator)
        return {"damage": damage}
    except StopIteration:
        return {"message": "No more damage events"}
if __name__ == "__main__":
    uvicorn.run(app, port=8084)