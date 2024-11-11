speed = int(input('Enter the velocity of the car(km/h): '))
if speed > 80:
    print('You are past the speed limit!')
    print(f'Your fine is ${(speed - 80) * 7}')

print('Drive safely!')
