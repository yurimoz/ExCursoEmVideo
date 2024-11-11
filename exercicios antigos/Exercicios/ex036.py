value = float(input('How much is the house worth? $'))
salary = float(input('How much do you earn per month? $'))
years = int(input('In how many years do you plan on completing the payment? '))
months = years * 12
payback = value / months
ceiling = salary * 0.3

print(f'To pay for the house in {years} years you will have to pay ${payback:.2f} per month!')

if payback > ceiling:
    print('That is more than 30% of your monthly wage')
    print('Unfortunately your loan was denied')

else:
    print('Loan approved!')
