import uvicorn
from fastapi import FastAPI
import numpy as np
app = FastAPI()

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
class Order:
    def __init__(self, id, user, products):
        self.id = id
        self.user = user
        self.products = products

products = [
    Product(1, "Laptop", 1200.0, "Electronics"),
    Product(2, "Phone", 799.0, "Electronics"),
    Product(3, "Desk", 350.0, "Furniture"),
    Product(4, "Mouse", 25.0, "Electronics")
]
#11
def get_prices_array(products):
    return np.array([p.price for p in products], dtype=float)
prices_array = get_prices_array(products)
print("Prices:", prices_array)
#12
def get_mean_median(prices):
    mean_price = np.mean(prices)
    median_price = np.median(prices)
    return (round(mean_price, 2), median_price)
mean_median = get_mean_median(prices_array)
print("Mean & Median:", mean_median)
#13
def normalize_prices(prices):
    min_val = np.min(prices)
    max_val = np.max(prices)
    return (prices - min_val) / (max_val - min_val)
normalized = normalize_prices(prices_array)
print("Normalized:", normalized)
#14
def get_categories_array(products):
    return np.array([p.category for p in products])
categories = get_categories_array(products)
print(categories)
#15
def count_unique_categories(categories):
    return len(set(categories))
categories = np.array(["Electronics", "Clothing", "Electronics"])
result = count_unique_categories(categories)
print(result)
#16
def get_expensive_products(products, prices):
    mean_price = np.mean(prices)
    return [p for p in products if p.price > mean_price]
prices = np.array([p.price for p in products])
result = get_expensive_products(products, prices)
for p in result:
    print(p.name, p.price)
#17
def apply_discount(prices):
    return prices * 0.9
prices=apply_discount(prices)
#prices = np.array([1200.0, 25.0, 450.0])
discounted = apply_discount(prices)
print(discounted)
#18
def build_orders_matrix(orders):
    totals = []
    for order in orders:
        total_price = sum(p.price for p in order.products)
        totals.append([total_price])
    return np.array(totals)
orders = [
    Order(1, "u1", [
        Product(1, "Laptop", 1200.0, "Electronics")
    ]),
    Order(2, "u2", [
        Product(2, "Mouse", 25.0, "Electronics"),
        Product(1, "Laptop", 1200.0, "Electronics")
    ])
]
print(build_orders_matrix(orders))
#19
def average_order_per_user(order_totals):
    return float(np.mean(order_totals))
order_totals = np.array([1200.0, 1225.0])
result = average_order_per_user(order_totals)
print(result)
#20
def get_expensive_order_indices(order_totals):
    return np.where(order_totals > 1000)[0]
order_totals = np.array([1200.0, 900.0, 1500.0])
result = get_expensive_order_indices(order_totals)
print(result)

#11
@app.get("/prices")
def api_prices():
    return prices_array.tolist()
#12
@app.get("/stats")
def api_stats():
    return {
        "mean": mean_median[0],
        "median": mean_median[1]
    }
#13
@app.get("/normalize")
def api_normalize():
    return normalized.tolist()
#14
@app.get("/categories")
def api_categories():
    return categories.tolist()
#15
@app.get("/categories/unique")
def api_unique_categories():
    return result
#16
@app.get("/expensive")
def api_expensive():
    return [{"name": p.name, "price": p.price} for p in result]
#17
@app.get("/discount")
def api_discount():
    return discounted.tolist()
#18
@app.get("/orders/matrix")
def api_orders_matrix():
    return build_orders_matrix(orders).tolist()
#19
@app.get("/orders/average")
def api_avg_order():
    return result
#20
@app.get("/orders/expensive-indices")
def api_expensive_indices():
    return result

if __name__ == "__main__":
    uvicorn.run(app, port=7076)




