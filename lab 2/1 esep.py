logs_content = """2026-02-01;user_1;LOGIN
2026-02-01;user_2;LOGIN
2026-02-01;user_1;BUY;120
2026-02-01;user_3;LOGIN
2026-02-01;user_2;BUY;300
2026-02-01;user_1;BUY;50
2026-02-01;user_2;LOGOUT"""
with open("shop_logs.txt", "w", encoding="utf-8") as f:
    f.write(logs_content)
users = set()
total_pokup = 0
total_sum = 0
rasxod = {}
with open("shop_logs.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts=line.split(";")
        user_id=parts[1]
        action=parts[2]
        users.add(user_id)
        if action=="BUY":
            total_pokup+=1
            summ=float(parts[3])
            total_sum+=summ
            if user_id in rasxod:
                rasxod[user_id]+=summ
            else:
                rasxod[user_id]=summ
max_user=""
max_spent=0
for user in rasxod:
    if rasxod[user]>max_spent:
        max_spent=rasxod[user]
        max_user=user
if total_pokup>0:
    average_check=total_sum/total_pokup
else:
    average_check=0
with open("data.txt", "w", encoding="utf-8") as file:
    file.write(f"Уникальных пользователей: {len(users)}\n")
    file.write(f"Всего покупок: {total_pokup}\n")
    file.write(f"Общая сумма: {total_sum}\n")
    file.write(f"Самый активный покупатель: {max_user}\n")
    file.write(f"Средний чек: {average_check}\n")
print("Отчет успешно создан!")