## Dictionary ##
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 1:'num' }

student['phone'] = '480-234-1234'
student.update({'name': 'Jane', 'age': 29, 'phone': '123-456-7890'})

del student['age']
num = student.pop(1)

len(student)
student.keys()
student.values()

student['gender'] = 'Female'

student.items()

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)

print(num)
print(student)