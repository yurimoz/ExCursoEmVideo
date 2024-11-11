price = 0
distance = int(input('Whats the distance traveled(km): '))

if distance > 200:
    price = distance * 0.45
else:
    price = distance * 0.5

print(f'Your fare is ${price:.2f}')
