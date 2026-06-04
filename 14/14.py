#1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("Сорта мороженого:")
        for f in self.flavors:
            print(f)


ice = IceCreamStand("Мороженко", "Кафе-мороженое", ["Ванильное", "Шоколадное", "Клубничное"])
ice.show_flavors()

#2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.time = time
        self.stick = []
        self.soft = []

    def show_flavors(self):
        print("Сорта мороженого:")
        for f in self.flavors:
            print(f)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Добавлен сорт: {flavor}")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Удален сорт: {flavor}")
        else:
            print(f"Сорта {flavor} нет в списке")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт {flavor} есть в наличии")
        else:
            print(f"Сорта {flavor} нет в наличии")

    def add_stick(self, flavor):
        self.stick.append(flavor)
        print(f"Мороженое на палочке {flavor} добавлено")

    def add_soft(self, flavor):
        self.soft.append(flavor)
        print(f"Мягкое мороженое {flavor} добавлено")

    def show_stick(self):
        print("Мороженое на палочке:", end=" ")
        for s in self.stick:
            print(s, end=" ")
        print()

    def show_soft(self):
        print("Мягкое мороженое:", end=" ")
        for s in self.soft:
            print(s, end=" ")
        print()


ice = IceCreamStand("Мороженко", "Кафе-мороженое", ["Ванильное", "Шоколадное"], "Центр", "10:00-22:00")

ice.show_flavors()
ice.add_flavor("Клубничное")
ice.remove_flavor("Ванильное")
ice.check_flavor("Шоколадное")

ice.add_stick("Фруктовый лед")
ice.add_soft("Карамельное")
ice.show_stick()
ice.show_soft()

#3
from tkinter import *
from tkinter import messagebox


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    def show_flavors(self):
        if len(self.flavors) == 0:
            return "Список пуст"
        return "\n".join(self.flavors)


ice = IceCreamStand("Мороженко", "Кафе-мороженое")

def add_flavor():
    flavor = flavor_input.get()
    if flavor == "":
        messagebox.showerror("Ошибка", "Введите сорт мороженого")
    else:
        ice.add_flavor(flavor)
        info["text"] = ice.show_flavors()
        flavor_input.delete(0, END)

def remove_flavor():
    flavor = flavor_input.get()
    if flavor in ice.flavors:
        ice.remove_flavor(flavor)
        info["text"] = ice.show_flavors()
        flavor_input.delete(0, END)
    else:
        messagebox.showerror("Ошибка", "Такого сорта нет")

root = Tk()

root.title("Кафе-мороженое")
root.geometry("400x300")
root["bg"] = "#fafafa"
root.resizable(width=False, height=False)

frame_top = Frame(root, bg="#40E0D0", bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg="#40E0D0", bd=5)
frame_bottom.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.3)

flavor_input = Entry(frame_top, bg="white", font=20)
flavor_input.pack(pady=10)

btn_add = Button(frame_top, text="Добавить сорт", command=add_flavor)
btn_add.pack()

btn_remove = Button(frame_top, text="Удалить сорт", command=remove_flavor)
btn_remove.pack(pady=5)

info = Label(
    frame_bottom,
    text="Список мороженого",
    bg="#40E0D0",
    font=15,
    justify=LEFT
)

info.pack()
root.mainloop()
