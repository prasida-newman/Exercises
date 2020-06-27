# Code your solution here
string = 'BYTE ACADEMY'
data = ''
for i in string:
    if i in('A','E','I','O','U'):
        data = data
    else:
        data += i
print(data)