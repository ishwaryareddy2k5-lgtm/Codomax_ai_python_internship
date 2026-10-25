marks = [85, 78, 92, 88, 80]
total = sum(marks)
percentage = total / len(marks)

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Needs improvement"

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
