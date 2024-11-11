import random
student1 = input('Enter the name of the first student: ').title()
student2 = input('Enter the name of the second student: ').title()
student3 = input('Enter the name of the third student: ').title()
student4 = input('Enter the name of the fourth student: ').title()
students = [student1, student2, student3, student4]
print(random.choice(students))
