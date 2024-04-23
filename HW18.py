import json

people = {
    "123456": ("Иван", 25),
    "654321": ("Алена", 30),
    "111222": ("Сергей", 40),
    "222333": ("Мария", 28),
    "333444": ("Дмитрий", 35),
}

for key, value in people.items():
    first_type = type(value[0])
    second_type = type(value[1])

    print(f"Ключ: {key}, Типы данных: ({first_type}, {second_type})")
file_path = "D:/people_dict.json"
with open(file_path, 'w') as json_file:
    json.dump(people, json_file)

print(file_path)
