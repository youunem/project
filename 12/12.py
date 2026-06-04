# #1
import json
with open('12.json', encoding='utf-8') as fp:
    data = json.load(fp)

for p in data['products']:
    print(f"Название: {p['name']}")
    print(f"Цена: {p['price']}")
    print(f"Вес: {p['weight']}")
    if p['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()

#2
import json

with open('12.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)

name = input("Название продукта: ")
price = int(input("Цена продукта: "))
weight = int(input("Вес продукта: "))
available = input("Есть в наличии, писать только Да или Нет: ").lower() == "да"

new = {
    "name": name,
    "price": price,
    "weight": weight,
    "available": available
}

data['products'].append(new)

with open('12.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp)

for p in data['products']:
    print(f"Название: {p['name']}")
    print(f"Цена: {p['price']}")
    print(f"Вес: {p['weight']}")
    if p['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()

#3
ru = {}

with open('12.3.txt', 'r', encoding='utf-8') as f:
    for i in f:
        if '-' in i:
            a, b = i.strip().split(' - ')
            for c in b.split(', '):
                if c in ru:
                    ru[c].append(a)
                else:
                    ru[c] = [a]

with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for r in sorted(ru.keys()):
        s = r + " – "
        for e in sorted(ru[r]):
            s = s + e + ", "
        s = s[:-2] + "\n"
        f.write(s)