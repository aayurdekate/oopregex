import abc
import re

class Transport(abc.ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abc.abstractmethod
    def display_info(self):
        pass

    def validate_year(self, year):
        year_pattern = r"^\d{4}$"
        if not re.match(year_pattern, str(year)):
            raise ValueError("Year must be a four-digit number")

class Vehicle(Transport):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.validate_year(year)

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Number of Doors: {self.number_of_doors}")

if __name__ == "__main__":
    try:
        car = Car("Toyota", "Camry", 2023, 4)
        car.display_info()

        vehicle = Vehicle("Honda", "Civic", 2022)
        vehicle.display_info()

    except ValueError as e:
        print(e)