from logicfile import validate_marks, calculate_average, determine_grade
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = []
subjects = int(input("Enter number of subjects: "))
for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
if not validate_marks(marks):
    print("Error: All marks must be between 0 and 100.")
else:
    average = calculate_average(marks)
    grade = determine_grade(average)
    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")