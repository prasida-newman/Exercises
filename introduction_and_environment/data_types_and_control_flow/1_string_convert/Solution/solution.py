# Code your solution here
print('string:')
string = input()

if string.upper() == string:
    data = string.lower()
elif string.lower() == string:
    data = string.upper()
print(data)