import uvicorn
from fastapi import FastAPI

app = FastAPI()

class Player:
    def __init__(self, id: int, hp: int):
        self.id = id
        self.__hp = hp
        self.__inventory = []

    @property
    def hp(self):
        return self.__hp

    @property
    def inventory(self):
        return self.__inventory

    def take_damage(self, amount: int):
        self.__hp = max(0, self.__hp - amount)

    def heal(self, amount: int):
        self.__hp += amount

    def add_item(self, item: str):
        self.__inventory.append(item)

    def remove_item(self, item: str):
        if item in self.__inventory:
            self.__inventory.remove(item)


player = Player(1, 100)

@app.get("/player")
def get_player():
    return {
        "id": player.id,
        "hp": player.hp,
        "inventory": player.inventory
    }

@app.post("/damage/{value}")
def damage(value: int):
    player.take_damage(value)
    return {"hp": player.hp}

@app.post("/heal/{value}")
def heal(value: int):
    player.heal(value)
    return {"hp": player.hp}

@app.post("/add_item/{item}")
def add_item(item: str):
    player.add_item(item)
    return {"inventory": player.inventory}

@app.post("/remove_item/{item}")
def remove_item(item: str):
    player.remove_item(item)
    return {"inventory": player.inventory}
if __name__ == "__main__":
    uvicorn.run(app, port=8045)