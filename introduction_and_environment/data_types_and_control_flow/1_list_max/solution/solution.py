L = [1,2,3,4,1337]
LIST_MAX = []
if L[0] > L[1]:
    LIST_MAX = L[0]
if L[1] > L[2]:
    LIST_MAX = L[1]
if L[2] > L[3]:
    LIST_MAX = L[2]
if L[3] > L[4]:
    LIST_MAX = L[3]
else:
    LIST_MAX = L[4]

print(LIST_MAX)