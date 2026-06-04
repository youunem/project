#1
from PIL import Image

img = Image.open("открытка.jpg")
cropped = img.crop((180, 75, 360, 260))
cropped.save("открытка_обрезанная.jpg")

#2
from PIL import Image

d = {"Новый год": "НГ.jpg", "С 8 марта": "8.jpg", "С днем рождения": "открытка.jpg"}
n = input("к какому празднику нужна открытка?: ")

if n in d:
 img = Image.open(d[n])
 img.show()
else:
    print("такой нету")

#3
from PIL import Image, ImageDraw, ImageFont
import random

d = {"Новый год": "НГ.jpg", "С 8 марта": "8.jpg", "С днем рождения": "открытка.jpg"}
n = input("К какому празднику нужна открытка? ")

if n in d:
 img = Image.open(d[n])
 name = input("Введите имя: ")
 text = name + ", поздравляю!"

 d2 = ImageDraw.Draw(img)
 p = ImageFont.truetype("arialbd.ttf", 20)

 c = ["red", "blue", "green", "purple", "orange", "pink"]
 r = random.choice(c)
 d2.text((60, 20), text, fill=r, font=p)

 img.save(name + ".png")
else:
 print("такой нету")