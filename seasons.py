#Spring months: 3,4,5
#Summer months: 6,7,8
#Fall months: 9,10,11
#Winter months: 12,1,2
month=int(input('enter the month:'))
if month in [3,4,5]:
    print('it is spring')
elif month in [6,7,8]:
    print('it is summer')
elif month in [9,10,11]:
    print('it is fall')
elif month in [12,1,2]:
    print('it is winter')
else:
    print('not a valid month......')
