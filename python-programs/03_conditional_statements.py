"""Determine a grade using conditional statements."""

marks = float(input("Enter marks from 0 to 100: "))

if not 0 <= marks <= 100:
    print("Please enter marks between 0 and 100.")

elif marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 40:
    print("Grade: D")

else:
    print("Grade: F")