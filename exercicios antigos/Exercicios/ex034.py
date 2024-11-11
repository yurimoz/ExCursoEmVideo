salary = float(input('Enter your salary: $'))

if salary > 1250:
    rais = 10
    newsalary = salary * 1.1  # 10% raise

else:
    rais = 15
    newsalary = salary * 1.15    # 15% raise

print(f'You got a {rais}% raise! Your new salary is ${newsalary:.2f}')
