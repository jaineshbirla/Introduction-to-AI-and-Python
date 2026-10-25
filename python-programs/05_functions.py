"""Demonstrate functions in Python."""


def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


person = input("Enter your name: ").strip()

if not person:
    person = "Learner"

print(greet(person))

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

result = add(first, second)

print("Sum:", result)