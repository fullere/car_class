# Elizabeth Fuller
# 11/11/19
# Car Class


class Car:
    def __init__(self, make, model, color, year, mileage, price):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
        self.price = price

    def description(self):
        print(f"""The car's attributes:
Make: {self.make}
Model: {self.model}
Color: {self.color}
Year: {self.year}
Mileage: {self.mileage}
Price: {self.price}""")

    def change_color(self):
        new_color = input("Change car color to: ")
        self.color = new_color


    def update_odometer(self):
        new_reading = int(input("Enter new odometer reading: "))
        self.mileage = new_reading
