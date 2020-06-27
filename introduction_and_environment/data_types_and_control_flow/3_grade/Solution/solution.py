# Code your solution here
print('Marks:')
mark = int(input())
grade = ''

if mark >=90:
    grade = 'A+ GRADE'
elif mark >=70 and mark <90:
    grade = 'B GRADE'
elif mark >= 50 and mark <70:
    grade = 'C GRADE'
elif mark >= 35 and mark <50:
    grade = 'D GRADE'
else:
    grade = 'FAIL'

print(grade)