# Code your solution here
cheese = 'string'
please = 'string'
counter = 0

try:
    print(cheese - please)
except:
    counter +=1
try:
    cheese + please
except:
    counter +=1
try:
    cheese + 1
except:
    counter +=1
try:
    cheese * please
except:
    counter +=1
try:
    cheese * 2
except:
    counter +=1
try:
    cheese / please
except:
    counter +=1
try: 
    cheese ** please
except:
    counter +=1
try:
    cheese // please
except:
    counter +=1
try:
    cheese % please
except:
    counter +=1
    
STR_ARITHMETIC = 9 - counter
print(STR_ARITHMETIC)
