# Code your solution here
print('word:')
line = input()
w = "" 
for i in line: 
    w = i + w 
    if (line==w): 
        is_palindrome = 'YES'
    else:
        is_palindrome = 'NO'
print(is_palindrome)