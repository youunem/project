#1
from PIL import Image, ImageFilter
import os

os.mkdir("papka")

for f in os.listdir("."):
    if f.endswith(".jpg") and not os.path.isdir(f):
        im = Image.open(f)
        n = im.filter(ImageFilter.CONTOUR)
        n.save("papka/new_" + f)

#2
from PIL import Image
import os

for f in os.listdir("."):
    if f.endswith(".jpg") or f.endswith(".png"):
        img = Image.open(f)
        img.show()
        print("Размер:", img.size)
        print("Формат:", img.format)
        print("Цветовая модель:", img.mode)

#3
import csv
sum = 0
print("Нужно купить:")

with open('11.csv', newline="", encoding='utf-8') as fp:
    r = csv.reader(fp)
    next(r)
    for i in r:
        p = i[0]
        k = int(i[1])
        c = int(i[2])
        s = k * c
        sum += s
        print(f"{p} - {k} шт. за {c} руб.")

print(f"Итоговая сумма: {sum} руб.")
