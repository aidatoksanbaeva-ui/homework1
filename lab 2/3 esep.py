import json
orders_data=[
    {
        "order_id":1,
        "user": "Ali",
        "items": ["phone", "case"],
        "total":300000
    },
    {
        "order_id":2,
        "user": "Dana",
        "items": ["laptop"],
        "total":800000
    },
    {
        "order_id":3,
        "user": "Ali",
        "items": ["mouse", "keyboard"],
        "total":70000
    }
]
with open("orders.json", "w") as f:
    json.dump(orders_data, f, indent=4)
total_revenue = 0
user_orders={}
item_count={}
max_order_total=0
top_user=""
with open("orders.json", "r") as f:
    orders=json.load(f)
for order in orders:
    user=order["user"]
    total=order["total"]
    items=order["items"]
    total_revenue+=total
    if user not in user_orders:
        user_orders[user]=1
    else:
        user_orders[user]+=1
    if total>max_order_total:
        max_order_total=total
        top_user=user
    for item in items:
        if item not in item_count:
            item_count[item]=1
        else:
            item_count[item]+=1
most_popular_item=""
max_count=0
for item in item_count:
    if item_count[item]>max_count:
        max_count=item_count[item]
        most_popular_item=item
summary={
    "total_revenue":total_revenue,
    "top_user":top_user,
    "most_popular_item":most_popular_item,
    "total_orders": len(orders),
}
with open("summary.json", "w") as f:
    json.dump(summary, f, indent=4)
print("Total revenue:", total_revenue)
print("user orders:", user_orders)
print("item count:", sum(item_count.values()))
print("top user:", top_user)
print("most popular item:", most_popular_item)

