# Code your solution here
print('shape:')
figure = str(input()).title()
data = 0
shapes = {'Triangle':3 , 'Quadrilateral':4 , 'Pentagon':5 , 'Hexagon':6, 'Heptagon':7, 'Octagon':8, 'Nonagon':9}
try:
    data = shapes[figure]
except:
    print('enter different shape')
print(data)
