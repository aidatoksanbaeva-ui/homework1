import uvicorn
from fastapi import FastAPI
from datetime import datetime

class Event:
    def __init__(self, id: int, name: str, timestamp: datetime):
        self.id = id
        self.name = name
        self.timestamp = timestamp

    def __repr__(self):
        return f"Event(id={self.id}, name='{self.name}', timestamp='{self.timestamp}')"

class EventIterator:
    def __init__(self, events: list[Event]):
        self._events = events
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._events):
            event = self._events[self._index]
            self._index += 1
            return event
        else:
            raise StopIteration

app = FastAPI()

events = [
    Event(1, "Login", datetime.now()),
    Event(2, "Logout", datetime.now()),
    Event(3, "Purchase", datetime.now())
]

event_iterator = EventIterator(events)

@app.get("/next_event")
def get_next_event():
    try:
        event = next(event_iterator)
        return {"id": event.id, "name": event.name, "timestamp": str(event.timestamp)}
    except StopIteration:
        return {"message": "No more events"}
if __name__ == "__main__":
    uvicorn.run(app, port=7021)