import random

salary = int(input("Какая у вас зарплата? "))
bonus = random.choice([True, False])

if bonus:
    salary += random.randint(100, 5000)

print(f'${salary}')
