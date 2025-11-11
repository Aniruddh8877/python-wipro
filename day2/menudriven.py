#menu driven calculator usein match-cast

num1 =float(input('Enter num 1: '))
num2 =float(input('Enter num 2: '))

print('\n')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')

choice = int(input('Enter your choice: '))

match choice:
     case 1:
          print('Addition: ',num1 + num2)
     case 2:
          print('Subtraction: ',num1 - num2)
     case 3:
          print('Multiplication:' ,num1 * num2)
     case 4:
          print( 'Division: ',num1 / num2)
     case _:
          print('Invalid choice')