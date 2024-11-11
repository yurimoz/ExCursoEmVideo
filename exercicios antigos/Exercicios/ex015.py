rentdays = int(input('How many days was the car rented? '))
km = float(input('How many km did it run? '))
price = (rentdays * 60) + (km * 0.15)
print(f'Total price: ${price:.2f}')
