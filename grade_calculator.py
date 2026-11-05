
# Grade Calculator Program

# Step 1: Take student name
name = input("Enter student name: ")

# Step 2: Take marks for three subjects
math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))

# Step 3: Check whether marks are valid
if (math < 0 or math > 100 or
    english < 0 or english > 100 or
    python < 0 or python > 100):

    print("Invalid marks! Marks must be between 0 and 100.")

else:
    # Step 4: Calculate average marks
    average = (math + english + python) / 3

    # Step 5: Determine grade
    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    # Step 6: Display result
    print("\nStudent Name:", name)
    print("Average Marks:", round(average, 2))
    print("Final Grade:", grade)
