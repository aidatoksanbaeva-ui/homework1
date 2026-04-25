import uvicorn
import pandas as pd
from datetime import date
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category


class User:
    def __init__(self, id, name, email, registration_date=None):
        self.id = id
        self.name = name
        self.email = email
        self.registration_date = registration_date or str(date.today())

users = [
    User(1, "John Doe", "john@example.com"),
    User(2, "Alice", "alice@example.com"),
]

products = [
    Product(1, "Laptop", 1200.0, "Electronics"),
    Product(2, "Mouse", 25.0, "Electronics"),
    Product(3, "T-Shirt", 20.0, "Clothing"),
]

users_df = pd.DataFrame({
    "user_id": [1, 2],
    "user_name": ["John", "Alice"],
})

orders_df = pd.DataFrame({
    "order_id":    [101,         102,       103,       104],
    "user_id":     [1,           2,         1,         2],
    "user_name":   ["John",      "Alice",   "John",    "Alice"],
    "total":       [1200,        25,        500,       75],
    "total_price": [1200,        25,        500,       75],
    "category":    ["Electronics","Clothing","Clothing","Electronics"],
})

products_df = pd.DataFrame({
    "product_name": ["Laptop", "Mouse", "Shirt"],
    "category":     ["Electronics", "Electronics", "Clothing"],
    "price":        [1200, 25, 20],
})

# 21
def create_users_dataframe(users_list):
    return pd.DataFrame({
        "id":                [u.id for u in users_list],
        "name":              [u.name for u in users_list],
        "email":             [u.email for u in users_list],
        "registration_date": [u.registration_date for u in users_list],
    })

# 22
def create_products_dataframe(products_list):
    return pd.DataFrame({
        "id":       [p.id for p in products_list],
        "name":     [p.name for p in products_list],
        "category": [p.category for p in products_list],
        "price":    [p.price for p in products_list],
    })

# 23
def merge_users_orders(u_df, o_df):
    merged = pd.merge(u_df, o_df, on="user_id")
    return merged[["order_id", "user_name", "total"]]

# 24
def filter_orders_by_total(df, value):
    return df[df["total"] > value]

# 25
def group_orders_by_user(df):
    return (
        df.groupby("user_name", as_index=False)["total"]
        .sum()
        .rename(columns={"total": "total_sum"})
    )

# 26
def average_order_by_user(df):
    result = df.groupby("user_name")["total"].mean().reset_index()
    result.columns = ["user_name", "mean_total"]
    return result

# 27
def count_orders_by_user(df):
    result = df.groupby("user_name")["order_id"].count().reset_index()
    result.columns = ["user_name", "orders_count"]
    return result

# 28
def mean_price_by_category(df):
    result = df.groupby("category")["price"].mean().reset_index()
    result.columns = ["category", "mean_price"]
    return result

# 29
def add_discount_column(df):
    df = df.copy()
    df["discounted_price"] = df["price"] * 0.9
    return df

# 30
def sort_products_by_price(df):
    return df.sort_values(by="price", ascending=False)

# 31
def add_quantity_column(df):
    df = df.copy()
    df["quantity"] = 1
    return df

# 32
def add_total_price(df):
    df = df.copy()
    df["total_price"] = df["price"] * df["quantity"]
    return df

# 33
def filter_electronics(df):
    return df[df["category"] == "Electronics"]


# 34
def count_products_by_category(df):
    result = df.groupby("category")["product_name"].count().reset_index()
    result.columns = ["category", "count"]
    return result


# 35
def mean_price_by_category_products(df):
    result = df.groupby("category")["price"].mean().reset_index()
    result.columns = ["category", "mean_price"]
    return result


# 36
def sort_orders_by_price(df):
    return df.sort_values(by="total_price", ascending=False)


# 37
def top_n_orders(df, n=3):
    return df.sort_values(by="total_price", ascending=False).head(n)


# 38
def merge_orders_users(u_df, o_df):
    merged = pd.merge(u_df, o_df, on="user_id")
    return merged[["order_id", "user_name", "total_price"]]


# 39
def mean_order_by_user(df):
    result = df.groupby("user_name")["total_price"].mean().reset_index()
    result.columns = ["user_name", "mean_total"]
    return result


# 40
def count_orders_by_user2(df):
    result = df.groupby("user_name")["order_id"].count().reset_index()
    result.columns = ["user_name", "orders_count"]
    return result


# 41
def max_order_by_user(df):
    result = df.groupby("user_name")["total_price"].max().reset_index()
    result.columns = ["user_name", "max_order"]
    return result


# 42
def unique_categories_by_user(df):
    result = df.groupby("user_name")["category"].nunique().reset_index()
    result.columns = ["user_name", "unique_categories"]
    return result


# 43
def add_vip_column(df):
    df = df.copy()
    df["VIP"] = df["total_sum"] > 1000
    return df


# 44
def sort_users(df):
    return df.sort_values(by=["total_sum", "mean_total"], ascending=[False, True])


# 45
def final_report(df):
    grouped = df.groupby("user_name")
    result = grouped.agg(
        total_orders=("order_id", "count"),
        total_sum=("total_price", "sum"),
        mean_total=("total_price", "mean"),
        max_order=("total_price", "max"),
        unique_categories=("category", "nunique"),
    ).reset_index()
    result["VIP"] = result["total_sum"] > 1000
    return result

def html_wrap(title: str, table_html: str) -> str:
    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            h2   {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px 12px; text-align: left; }}
            th {{ background: #4a90d9; color: white; }}
            tr:nth-child(even) {{ background: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h2>{title}</h2>
        {table_html}
    </body>
    </html>
    """

# 21
@app.get("/users", response_class=HTMLResponse)
def api_users():
    return html_wrap("Users", create_users_dataframe(users).to_html(index=False))
# 22
@app.get("/products", response_class=HTMLResponse)
def api_products():
    return html_wrap("Products", create_products_dataframe(products).to_html(index=False))
# 23
@app.get("/merge-users-orders", response_class=HTMLResponse)
def api_merge_users_orders():
    return html_wrap("Merged Users & Orders", merge_users_orders(users_df, orders_df).to_html(index=False))
# 24
@app.get("/filter-orders", response_class=HTMLResponse)
def api_filter_orders():
    df = merge_users_orders(users_df, orders_df)
    return html_wrap("Filtered Orders (total > 100)", filter_orders_by_total(df, 100).to_html(index=False))


# 25
@app.get("/group-orders", response_class=HTMLResponse)
def api_group_orders():
    df = merge_users_orders(users_df, orders_df)
    return html_wrap("Group Orders by User", group_orders_by_user(df).to_html(index=False))


# 26
@app.get("/average-orders", response_class=HTMLResponse)
def api_average_orders():
    df = merge_users_orders(users_df, orders_df)
    return html_wrap("Average Order by User", average_order_by_user(df).to_html(index=False))


# 27
@app.get("/count-orders", response_class=HTMLResponse)
def api_count_orders():
    df = merge_users_orders(users_df, orders_df)
    return html_wrap("Count Orders by User", count_orders_by_user(df).to_html(index=False))


# 28
@app.get("/mean-price-category", response_class=HTMLResponse)
def api_mean_price_category():
    return html_wrap("Mean Price by Category", mean_price_by_category(create_products_dataframe(products)).to_html(index=False))


# 29
@app.get("/discount", response_class=HTMLResponse)
def api_discount():
    return html_wrap("Products with Discount", add_discount_column(create_products_dataframe(products)).to_html(index=False))


# 30
@app.get("/sort-products", response_class=HTMLResponse)
def api_sort_products():
    return html_wrap("Products Sorted by Price", sort_products_by_price(create_products_dataframe(products)).to_html(index=False))


# 31
@app.get("/add-quantity", response_class=HTMLResponse)
def api_add_quantity():
    return html_wrap("Orders with Quantity", add_quantity_column(orders_df).to_html(index=False))


# 32
@app.get("/total-price", response_class=HTMLResponse)
def api_total_price():
    df = add_quantity_column(orders_df)
    return html_wrap("Orders with Total Price", add_total_price(df).to_html(index=False))


# 33
@app.get("/electronics", response_class=HTMLResponse)
def api_electronics():
    return html_wrap("Electronics Products", filter_electronics(products_df).to_html(index=False))


# 34
@app.get("/count-products", response_class=HTMLResponse)
def api_count_products():
    return html_wrap("Count Products by Category", count_products_by_category(products_df).to_html(index=False))


# 35
@app.get("/mean-price", response_class=HTMLResponse)
def api_mean_price():
    return html_wrap("Mean Price by Category", mean_price_by_category_products(products_df).to_html(index=False))


# 36
@app.get("/sort-orders", response_class=HTMLResponse)
def api_sort_orders():
    return html_wrap("Orders Sorted by Price", sort_orders_by_price(orders_df).to_html(index=False))


# 37
@app.get("/top-orders", response_class=HTMLResponse)
def api_top_orders():
    return html_wrap("Top 3 Orders", top_n_orders(orders_df, 3).to_html(index=False))
# 38
@app.get("/merge-orders-users", response_class=HTMLResponse)
def api_merge_orders_users():
    return html_wrap("Merged Orders & Users", merge_orders_users(users_df, orders_df).to_html(index=False))
# 39
@app.get("/mean-order-user", response_class=HTMLResponse)
def api_mean_order_user():
    return html_wrap("Mean Order by User", mean_order_by_user(orders_df).to_html(index=False))
# 40
@app.get("/count-orders-user", response_class=HTMLResponse)
def api_count_orders_user():
    return html_wrap("Count Orders by User", count_orders_by_user2(orders_df).to_html(index=False))
# 41
@app.get("/max-order-user", response_class=HTMLResponse)
def api_max_order_user():
    return html_wrap("Max Order by User", max_order_by_user(orders_df).to_html(index=False))
# 42
@app.get("/unique-categories", response_class=HTMLResponse)
def api_unique_categories():
    return html_wrap("Unique Categories by User", unique_categories_by_user(orders_df).to_html(index=False))
# 43
@app.get("/vip", response_class=HTMLResponse)
def api_vip():
    df = final_report(orders_df)
    return html_wrap("VIP Users", add_vip_column(df).to_html(index=False))
# 44
@app.get("/sort-users", response_class=HTMLResponse)
def api_sort_users():
    df = final_report(orders_df)
    return html_wrap("Sorted Users", sort_users(df).to_html(index=False))
# 45
@app.get("/final-report", response_class=HTMLResponse)
def api_final_report():
    return html_wrap("Final Report", final_report(orders_df).to_html(index=False))


if __name__ == "__main__":
    uvicorn.run(app, port=8083)