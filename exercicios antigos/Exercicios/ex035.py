r1 = float(input('Enter the length of the first line: '))
r2 = float(input('Enter the length of the second line: '))
r3 = float(input('Enter the length of the third line: '))

sides = [r1, r2, r3]

if r1 >= (r2 + r3) or r2 > (r1 + r3) or r3 > (r1 + r2):
    print(f'{sides} cannot be a triangle :(')

else:
    print(f'{sides} can be a triangle!')
