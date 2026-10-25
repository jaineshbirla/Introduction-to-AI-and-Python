"""Calculate a student's average marks and grade."""


def calculate_average(marks):
    """Calculate the average of a list of marks."""
    return sum(marks) / len(marks)


def get_grade(average):
    """Determine the grade based on average marks."""

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 40:
        return "D"

    else:
        return "F"


def main():
    name = input("Enter student name: ").strip()

    if not name:
        name = "Student"

    marks = []

    # Input marks for three subjects
    for subject_number in range(1, 4):

        while True:
            try:
                mark = float(
                    input(
                        f"Enter marks for subject "
                        f"{subject_number} (0-100): "
                    )
                )

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    # Calculate average and grade
    average = calculate_average(marks)
    grade = get_grade(average)

    # Display results
    print("\n----- Student Result -----")
    print("Student Name:", name)
    print("Marks:", marks)
    print(f"Average Marks: {average:.2f}")
    print("Grade:", grade)


if __name__ == "__main__":
    main()