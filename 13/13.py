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


newRestaurant = Restaurant("Чайнис", "Китайская")

print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

#2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print()

    def open_restaurant(self):
        print("Ресторан открыт!")


newRestaurant1 = Restaurant("Чайнис", "Китайская")
newRestaurant2 = Restaurant("Пиццата", "Итальянская")
newRestaurant3 = Restaurant("Сушими", "Японская")

newRestaurant1.describe_restaurant()
newRestaurant2.describe_restaurant()
newRestaurant3.describe_restaurant()

#3
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print()

    def open_restaurant(self):
        print("Ресторан открыт!")

    rating = 1
    def change_rating(self, rating):
        self.rating = rating
        print(f'Рейтинг ресторана: {rating}')

newRestaurant = Restaurant("Чайнис", "Китайская")
newRestaurant.describe_restaurant()
newRestaurant.change_rating(5)