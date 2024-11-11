x = float(input('Enter the value of the first number: '))
y = float(input('Enter the value of the second number: '))
z = float(input('Enter the value of the third number: '))

biggest = 0
smallest = 0

if x >= y and x >= z:
    biggest = x

    if z >= y:
        smallest = y
    else:
        smallest = z

elif x >= y:
    biggest = z
    smallest = y

elif x >= z:
    biggest = y
    smallest = z

else:
    smallest = x

    if z >= y:
        biggest = z
    else:
        biggest = y

print(f'The biggest number you typed is {biggest:.2f} and the smallest is {smallest:.2f}')
