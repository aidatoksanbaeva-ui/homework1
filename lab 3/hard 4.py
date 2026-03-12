students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
grade_level = lambda x: "Отлично" if x >= 90 else ("Хорошо" if x >= 70 else "Удовлетворительно")
result = {name: grade_level(score) for name, score in students}
print(result)