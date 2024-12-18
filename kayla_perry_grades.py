def main():

    # Define the list for grades
    grades = []

    # Enter the first grade
    grade = int(input("Enter the first grade: "))

    # Begin while loop
    while grade != -1:
        grades.append(grade)
        grade = int(input("Enter the next grade: "))

    # Calculate the average
    average = sum(grades) / len(grades)

    # Sort the list in ascending order and descending order
    sorted_lh = sorted(grades)  # returns a new sorted list in ascending order
    sorted_hl = sorted(grades, reverse=True)  # returns a new sorted list in descending order

    # Find the highest and lowest grades
    highest = max(grades)
    lowest = min(grades)

    # Print results
    print()
    print(f"The grade average is: {average}")
    print(f"The grades from highest to lowest are: {sorted_hl}")
    print(f"The grades from lowest to highest are: {sorted_lh}")
    print(f"The highest grade is: {highest}")
    print(f"The lowest grade is: {lowest}")

main()
