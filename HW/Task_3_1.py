# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

#import pretty_errors

x=int(input('Enter the value of X: '))
y=int(input('Enter the value of Y: '))

if (x>0 and y>0):
    print('I quarter')
elif( x<0 and y>0):
    print('II quarter')
elif(x<0 and y<0):
    print('III quarter')
elif (x>0 and y<0):
    print('IV quarter')
else:
    print('Error.')