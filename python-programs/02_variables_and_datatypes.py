"""Demonstrate variables and Python data types."""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = 86.5
is_learning_python = True

print("\nStudent Details")
print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)
print("Learning Python:", is_learning_python)

print("\nData Types")
print("Name:", type(name).__name__)
print("Age:", type(age).__name__)
print("Percentage:", type(percentage).__name__)
print("Learning Python:", type(is_learning_python).__name__)