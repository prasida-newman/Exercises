# Code your solution here
month_dict = {'January':31, 'February':28, 'March': 31, 'April':30, 'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
print('Month:')
month = input()

try:
    print(month_dict[month])
except:
    print('month not found')