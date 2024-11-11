import math
alpha = float(input('Enter the value of the angle in degrees: '))
alpharadians = math.radians(alpha)
print(f'sin({alpha}º) = {math.sin(alpharadians):.2f}')
print(f'cos({alpha}º) = {math.cos(alpharadians):.2f}')
print(f'tan({alpha}º) = {math.tan(alpharadians):.2f}')
