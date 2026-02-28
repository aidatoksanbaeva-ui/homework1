import json
import csv
user_transaction_count = {}
suspicious_transactions = []
suspicious_users = set()
total_suspicious_amount = 0
with open("transactions.csv", "r", newline="")  as file:
    reader = csv.DictReader(file)
    for row in reader:
        user_id=row["user_id"]
        amount=int(row["amount"])
        if user_id not in user_transaction_count:
            user_transaction_count[user_id]=0
        user_transaction_count[user_id]+=1
        if amount>500000:
            suspicious_transactions.append(row)
            total_suspicious_amount+=amount
            suspicious_users.add(user_id)
for user, count in user_transaction_count.items():
    if count > 3:
        suspicious_users.add(user)
suspicious_users = list(suspicious_users)
with open("fraud_report.txt", "w", encoding="utf-8") as file:
    file.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
    file.write(f"Подозрительных пользователей: {len(suspicious_users)}\n")
    file.write(f"Список пользователей: {suspicious_users}\n")
    file.write(f"Общая сумма подозрительных операций: {total_suspicious_amount}\n")
with open("fraud_users.json", "w", encoding="utf-8") as file:
    json.dump(suspicious_users, file)
print("Подозрительных транзакций:", len(suspicious_transactions))
print("Подозрительных пользователей:", len(suspicious_users))
print("Список пользователей:", suspicious_users)
print("Общая сумма подозрительных операций:", total_suspicious_amount)
