"""Demonstrate list operations."""

subjects = [
    "Python",
    "Mathematics",
    "Artificial Intelligence"
]

print("Original subjects:", subjects)

print("First subject:", subjects[0])

# Add an item
subjects.append("Data Science")

# Update an item
subjects[1] = "Statistics"

print("\nUpdated subjects:")

for subject in subjects:
    print(subject)

print("\nTotal subjects:", len(subjects))