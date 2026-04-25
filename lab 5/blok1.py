import uvicorn
from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()
#1
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._name = name.strip().title()

        processed_email = email.strip().lower()

        if "@" not in processed_email:
            raise ValueError("Email-да '@' таңбасы болуы керек!")

        self._id = user_id
        self._email = processed_email

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

    def __del__(self):
        name = getattr(self, '_name', 'Unknown')
        print(f"User {name} deleted")
#2
    @classmethod
    def from_string(cls, data: str):
        parts = [item.strip() for item in data.split(',')]
        if len(parts) != 3:
            raise ValueError("Жолда 3 мән болуы керек: id, name, email")

        u_id = int(parts[0])
        u_name = parts[1]
        u_email = parts[2]
        return cls(u_id, u_name, u_email)
#3
class Product:
    def __init__(self, id:int, name:str, price:float, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category='{self.category}')"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        }
class ProductRequest(BaseModel):
    id: int
    name: str
    price: float
    category: str
#4
class Inventory:
    def __init__(self):
        self._products ={}
    def add_product(self, product:Product):
        if product.id in self._products:
            print(f"Product {product.id} already exists")
            return
        self._products[product.id] = product
    def remove_product(self, product_id:int):
        if product_id not in self._products:
            raise ValueError(f"Product {product_id} does not exist")
        del self._products[product_id]
    def get_product(self, product_id:int):
        if product_id not in self._products:
            raise ValueError(f"Product {product_id} does not exist")
        return self._products[product_id]
    def get_all_products(self):
        return list(self._products.values())
    def unique_products(self):
        return set(self._products.values())
    def to_dict(self):
        return dict(self._products)
#5
    def filter_by_price(self,min_price:float):
        is_expensive= lambda p: p.price>=min_price
        return [p for p in self._products.values() if is_expensive(p)]
#6
class Logger:
    def log_action(self,user: User, action: str, product: Product, filename: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line= f"{timestamp};{user._id};{action};{product.id}\n"
        with open(filename,"a") as f:
            f.write(line)
    def read_logs(self, filename: str):
        logs=[]
        with open(filename,"r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                logs.append({
                    "timestamp": parts[0],
                    "user._id": parts[1],
                    "action": parts[2],
                    "product_id": parts[3]
                })
        return logs
#7
class Order:
    def __init__(self, id:int, user:User):
        self.id = id
        self.user = user
        self.products: list = []
    def add_product(self, product:Product):
        self.products.append(product)
    def remove_product(self, product_id:int):
        for p in self.products:
            if p.id == product_id:
                self.products.remove(p)
                return
        raise ValueError(f"Product {product_id} not found in order")
    def total_price(self):
        return sum(p.price for p in self.products)
    def __str__(self):
        product_names = ", ".join(p.name for p in self.products)
        return (f"Order(id={self.id},user='{self.user._name}',"
                f"products=[{product_names}],total={self.total_price()})")
#8
    def most_expensive_products(self,n:int):
        return sorted(self.products, key=lambda p: p.price, reverse=True)[:n]
#9
def price_stream(products:list):
    for product in products:
        yield product.price
#10
class OrderIterator:
    def __init__(self, orders:list):
        self._orders = orders
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index>= len(self._orders):
            raise StopIteration
        order = self._orders[self._index]
        self._index += 1
        return order

u1=User(1, "Lee Mark ","leemark@Example.COM")
print(u1)

u2 = User.from_string("2, Alice Wonderland , alice@wonder.com")
print(u2)

p1=Product(1,"Laptop", 1200.0 ,"Electronics")
p2 = Product(2, "Phone",  799.0,  "Electronics")
p3 = Product(3, "Desk",     350.0, "Furniture")
p4 = Product(4, "Mouse",     25.0, "Electronics")
#4
inv=Inventory()
inv.add_product(p1)
inv.add_product(p2)
inv.add_product(p3)
inv.add_product(p4)
print("All products:")
print(p1)
print(p2)
print(p3)
print(p4)
print(inv.get_all_products())
print(inv.get_product(2))
print("Unique products:",len(inv.unique_products()))
print("to_dict keys:",list(inv.to_dict().keys()))
inv.remove_product(2)
print("after removing:",len(inv.get_all_products()))
#5
expensive = inv.filter_by_price(300.0)
print("Products >= 300.0:",[p.name for p in expensive])
#6
logger = Logger()
logger.log_action(u1, "purchase", p1, "log.txt")
logger.log_action(u1, "view",     p2, "log.txt")
logger.log_action(u1, "purchase", p2, "log.txt")
logs = logger.read_logs("log.txt")
for entry in logs:
    print(entry)
#7
order = Order(1,u1)
order.add_product(p1)
order.add_product(p2)
order.add_product(p3)
print(order)
order.remove_product(2)
print(order)
print("Total:",order.total_price())
#8
print("Most expensive:")
for p in order.most_expensive_products(2):
    print(p)
#9
print("Price stream:")
for price in price_stream([p1,p2,p3]):
    print(price)
#10
order2=Order(2,u1)
order2.add_product(p3)
iterator = OrderIterator([order,order2])
print("order iterator")
for order in iterator:
    print(order)

#1
@app.get("/1-user")
def task1_user():
    return {
        "id": u1._id,
        "name": u1._name,
        "email": u1._email
    }

#2
@app.get("/2-user-from-string")
def task2_user_from_string():
    u = User.from_string("2, Alice Wonderland , alice@wonder.com")
    return {"id": u._id, "name": u._name, "email": u._email}

#3
@app.get("/3-products")
def task3_products():
    return [p1.to_dict(), p2.to_dict(), p3.to_dict(), p4.to_dict()]

#4
@app.get("/4-inventory-all")
def task4_inventory_all():
    return [p.to_dict() for p in inv.get_all_products()]

#5
@app.get("/5-product/{product_id}")
def task5_get_product(product_id: int):
    return inv.get_product(product_id).to_dict()

#6
@app.get("/6-expensive")
def task6_expensive():
    return [p.to_dict() for p in inv.filter_by_price(300.0)]

#7
@app.get("/7-order")
def task7_order():
    return {
        "order_id": order.id,
        "user": order.user._name,
        "total": order.total_price(),
        "products": [p.to_dict() for p in order.products]
    }

#8
@app.get("/8-top-products")
def task8_top_products():
    return [p.to_dict() for p in order.most_expensive_products(2)]

#9
@app.get("/9-price-stream")
def task9_price_stream():
    return list(price_stream([p1, p2, p3]))

#10
@app.get("/10-orders")
def task10_orders():
    iterator = OrderIterator([order, order2])
    return [{"id": o.id, "user": o.user._name} for o in iterator]

if __name__ == "__main__":
    uvicorn.run(app, port=8654)