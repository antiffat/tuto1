# mutable - data can change
# immutable - data cannot change after the creation of variable
from platform import libc_ver
from tkinter.font import names

from setuptools.config.pyprojecttoml import load_file

print("-----------------")
city = "  Broclaw "
print(city)
print(city.strip())
print(city.upper())
print(city.strip().replace("B", "W"))

print("----------------")

print(city.strip().startswith("B"))
print(city.endswith("w"))
print(city.isdigit())
print(city.strip().isalpha())

password = "123@abc"
print("4" not in password)

print("-------------------")

age = 20
print(age > 18) # true or false

temperature = -5
print(temperature < 0)

score = 90
print(score >= 91)

lives = 1
print(lives <= 0)

name = " Maja"
print(name.strip() == "Maja")

country = "Poland"
print(country != "Poland")

age = 16
has_ticket = False
print(age > 18 and has_ticket)
print(age > 18 or has_ticket)

username = "admin"
password = "1234"
print(username == "admin" and password == "1234")

logged_in = False
print(not logged_in)

if not has_ticket:
    print("you cannot enter")