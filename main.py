num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
choice = input('''
Please select the type of operation you want to perform:
+ for addition
- for subtraction
/ for division
% for modulo
^ for square
''')
if choice == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)

elif choice == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)

elif choice == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)

elif choice == '%':
    print('{} % {} = '.format(num_1, num_2))
    print(num_1 % num_2)

elif choice == '^':
    print('{} ^ 2 = '.format(num_1))
    print(num_1**2)
    print('{} ^ 2 = '.format(num_2))
    print(num_2**2)

else:
    print('Enter a valid operator.')
