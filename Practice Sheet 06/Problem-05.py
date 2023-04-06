'''
A certain CS professor gives 100-point exams that are graded on the scale 90- 100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts an exam score as input and prints out the corresponding grade.
'''

marks = eval(input("Enter your marks: "))
if 100 >= marks >= 89.5:  # 90-100
    grade = 'A'
elif 89.5 > marks >= 79.5:  # 80-90
    grade = 'B'
elif 79.5 > marks >= 69.5:  # 70-80
    grade = 'C'
elif 69.5 > marks >= 59.5:  # 60-70
    grade = 'D'
elif 59.5 > marks >= 0:  # <60
    grade = 'F'
print("Your grade is:", grade)
