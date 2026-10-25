
# Student Grade Calculator

name = input("Enter student name: ")

marks = []

for i in range(1, 4):
    mark = float(input(f"Enter marks for subject {i} (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Please enter a value from 0 to 100.")
        raise SystemExit
    marks.append(mark)

total = sum(marks)
percentage = total / len(marks)

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
