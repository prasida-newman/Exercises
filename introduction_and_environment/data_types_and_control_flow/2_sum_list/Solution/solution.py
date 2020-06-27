# Code your solution here
list_a = [1,'a',2,'b']
total =0
for i in list_a:
    try:
        total +=i
    except:
        total +=0
print(total)
