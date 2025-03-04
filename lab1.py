# Zadanie 1
from collections import namedtuple


class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"Jestem {self.first_name}  {self.last_name}"


class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, salary: int, department: str) -> None:
        super().__init__(first_name, last_name, salary)
        self.department = department

    def get_department_info(self) -> str:
        return f"zarządzam działem {self.department}"


Employee1 = Employee("Jan", "Nowak", 10000)
Manager1 = Manager("Jan", "Kowalski", 20000, "IT")

print("-------------------------------")
print(Employee1.get_full_name())
print(Manager1.get_department_info())

# Zadanie2

Transaction = namedtuple("Transaction", ["transaction_id", "amount", "currency"])


class BankAccount:
    balance: int

    def __init__(self, balance: int) -> None:
        self.balance = balance

    def apply_transaction(self, Transaction: Transaction):
        self.balance += Transaction.amount


print("-------------------------------")
Transaction1 = Transaction(1, 50000, "USD")
konto = BankAccount(10000)
BankAccount.apply_transaction(konto, Transaction1)
print(konto.balance)

# Zadanie 3

from dataclasses import dataclass, field


@dataclass()
class Book:
    title: str
    author: str
    year: int
    price: float

    def apply_discount(self, discount):
        self.price = self.price - ((self.price * discount) / 100)


print("-------------------------------")
book1 = Book("W pustyni i w puszczy", "Henryk Sienkiewicz", 1911, 50)
book1.apply_discount(20)
print(book1.price)


# Zadanie 4

@dataclass()
class Product:
    name: str
    price: float
    category: str = field(default="General")

    def validate_price(self):
        if self.price < 0:
            raise (ValueError("nie mozna przyjac takiej wartosci"))
        else:
            pass


# Zadanie 5
from datetime import datetime


@dataclass()
class Car:
    brand: str
    model: str
    year: int

    def is_classic(self) -> bool:
        current_year = datetime.now().year
        if (current_year - self.year >= 25):
            return True
        else:
            return False


print("-------------------------------")

Audi = Car("Audi", "A4", 2005)
BMW = Car("BMW", "X", 1999)
print(Audi.is_classic())
print(BMW.is_classic())

print("-------------------------------")


class ElectricVehicle:
    fuel_type: str

    def __init__(self):
        self.fuel_type = "Electric"

    def fuel_type(self):
        return self.fuel_type


class GasolineVehicle:
    fuel_type: str

    def __init__(self):
        self.fuel_type = "Gasoline"

    def fuel_type(self):
        return self.fuel_type


class HybridCar(ElectricVehicle, GasolineVehicle):
    fuel_type: str

    def __init__(self):
        super().__init__()
        self.fuel_type = "Hybrid"


a = ElectricVehicle()
b = GasolineVehicle()
c = HybridCar()

print(a.fuel_type)
print(b.fuel_type)
print(c.fuel_type)
print("-------------------------------")


class Person:
    def introduce(self):
        return f"I am a person"


class Worker(Person):
    def introduce(self):
        return f"I am a worker"


class Student(Person):
    def introduce(self):
        return f"I am a student"


class WorkingStudent(Worker, Person):
    def introduce(self):
        return f"I am a working student"


print(WorkingStudent.introduce(Person))


class Animal:
    def __init__(self):
        pass

    def make_sound(self):
        return "some sound"


class Pet:
    def __init__(self):
        pass

    def is_domestic(self):
        return True


class Dog(Animal, Pet):
    def __init__(self):
        super().__init__()

    def make_sound(self):
        return f"bark, bark!"

    def is_domestic(self):
        return True


dog1 = Dog()
print(dog1.is_domestic())

print("-------------------------------")


class FlyingVehicle:
    def move(self) -> str:
        return "I fly"


class WaterVehicle:
    def move(self) -> str:
        return "I sail"


class AmphibiousVehicle(FlyingVehicle, WaterVehicle):
    def move(self, mode: str) -> str:
        if mode == "fly":
            return super(FlyingVehicle, self).move()
        elif mode == "sail":
            return super(WaterVehicle, self).move()


class Robot:
    def operate(self):
        return "Performing task"


class AI:
    def think(self):
        return "Processing data"


class Android(Robot, AI):
    def learn(self):
        return "Learning new tasks"


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


class IDGenerator:
    _current_id = 0

    @classmethod
    def generate_id(cls):
        cls._current_id += 1
        return cls._current_id


class Store:
    total_customers = 0

    @classmethod
    def add_customer(cls):
        cls.total_customers += 1

    @classmethod
    def get_total_customers(cls):
        return cls.total_customers


class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @classmethod
    def identity_matrix(cls, size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


class GameCharacter:
    default_health = 100

    def __init__(self):
        self.health = self.default_health

    def restore_health(self):
        self.health = self.default_health

    @classmethod
    def set_default_health(cls, new_value):
        cls.default_health = new_value


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class PaymentProcessor(ABC):
    @abstractmethod
    def authorize_payment(self, amount):
        pass

    @abstractmethod
    def capture_payment(self, amount):
        pass


class CreditCardPayment(PaymentProcessor):
    def authorize_payment(self, amount):
        print(f"Authorizing credit card payment of {amount}.")

    def capture_payment(self, amount):
        print(f"Capturing credit card payment of {amount}.")


class PayPalPayment(PaymentProcessor):
    def authorize_payment(self, amount):
        print(f"Authorizing PayPal payment of {amount}.")

    def capture_payment(self, amount):
        print(f"Capturing PayPal payment of {amount}.")


class Vehicle(ABC):
    @abstractmethod
    def max_speed(self):
        pass


class Car(Vehicle):
    def max_speed(self):
        return 200


class Bicycle(Vehicle):
    def max_speed(self):
        return 25


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass


class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to MySQL database.")

    def execute_query(self, query):
        print(f"Executing query on MySQL: {query}")


class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to PostgreSQL database.")

    def execute_query(self, query):
        print(f"Executing query on PostgreSQL: {query}")


class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


class Piano(Instrument):
    def play(self):
        print("Playing the piano.")


class Guitar(Instrument):
    def play(self):
        print("Playing the guitar.")
