import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    power: int

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        if item.id not in [i.id for i in self.items]:
            self.items.append(item)

    def remove_item(self, item_id: int):
        self.items = [item for item in self.items if item.id != item_id]

    def get_items(self):
        return self.items

    def unique_items(self):
        return [item.dict() for item in {item.id: item for item in self.items}.values()]

    def to_dict(self):
        return {item.id: item for item in self.items}

inventory = Inventory()
inventory.add_item(Item(id=1, name="Sword", power=10))
inventory.add_item(Item(id=2, name="Shield", power=5))
inventory.add_item(Item(id=3, name="Bow", power=7))
inventory.add_item(Item(id=1, name="Duplicate Sword", power=10))

@app.post("/add_item")
def add_item_endpoint(item: Item):
    inventory.add_item(item)
    return {"message": "Item added"}

@app.delete("/remove_item/{item_id}")
def remove_item_endpoint(item_id: int):
    inventory.remove_item(item_id)
    return {"message": "Item removed"}

@app.get("/items")
def get_items_endpoint():
    return inventory.get_items()

@app.get("/unique_items")
def unique_items_endpoint():
    return inventory.unique_items()

@app.get("/items_dict")
def items_dict_endpoint():
    return inventory.to_dict()
#uvicorn ex4:app --reload --port 8001
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8045)